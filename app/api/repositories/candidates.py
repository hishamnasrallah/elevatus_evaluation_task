from fastapi import HTTPException
import uuid
from fastapi.encoders import jsonable_encoder
from app.api.models.candidates import candidate_collection, CandidateModel
from core.exceptions.candidates import CandidateDoesNotExist, CandidateDoesUpdated
from bson import ObjectId
import csv
import io
from fastapi.responses import StreamingResponse


def create_candidate(request_body, request):
    request_dict = request_body.dict()
    new_uuid = uuid.uuid4()
    uuid_str = str(new_uuid)
    request_dict["uuid"] = uuid_str
    new_rec = request.app.database[candidate_collection].insert_one(request_dict)
    created_item = request.app.database[candidate_collection].find_one({
        "_id": new_rec.inserted_id
    })
    if new_rec.inserted_id:
        created_item['_id'] = str(new_rec.inserted_id)
        return created_item  # Return the inserted user data
    else:
        raise HTTPException(status_code=500, detail="Failed to insert user into the database")


def get_candidate(candidate_id, request):
    candidate_id = ObjectId(candidate_id)
    candidate = request.app.database[candidate_collection].find_one({"_id": candidate_id})
    if not candidate:
        raise CandidateDoesNotExist
    candidate["_id"] = str(candidate["_id"])
    return jsonable_encoder(candidate)


def get_candidates(request):
    documents = request.app.database[candidate_collection].find()
    candidates = []
    for document in documents:
        document["_id"] = str(document["_id"])
        candidates.append(document)
    if not candidates:
        raise CandidateDoesNotExist
    return jsonable_encoder(candidates)


# UpdateResult({'n': 1, 'nModified': 0, 'ok': 1.0, 'updatedExisting': True}, acknowledged=True)
# UpdateResult({'n': 0, 'nModified': 0, 'ok': 1.0, 'updatedExisting': False}, acknowledged=True)


def update_candidate(candidate_id, request_body, request):
    candidate_id_object = ObjectId(candidate_id)
    updated_candidate_dict = request_body.dict()

    updated_candidate = request.app.database[candidate_collection].update_one(
        {"_id": candidate_id_object},
        {"$set": updated_candidate_dict}
    )
    if updated_candidate.matched_count == 0:
        raise CandidateDoesNotExist
    if updated_candidate.matched_count == 1 and updated_candidate.modified_count == 1:
        updated_candidate_dict['_id'] = candidate_id
        return jsonable_encoder(updated_candidate_dict)
    else:
        raise CandidateDoesUpdated


def delete_candidate(candidate_id, request):
    candidate_id_object = ObjectId(candidate_id)
    deleted_candidate = request.app.database[candidate_collection].find_one_and_delete({"_id": candidate_id_object})
    if deleted_candidate:
        deleted_candidate['_id'] = candidate_id
        return jsonable_encoder(deleted_candidate)
    else:
        raise CandidateDoesNotExist


def get_candidate_filter(keyword, request):
    all_fields = list(CandidateModel.__annotations__.keys())

    query = {}

    if keyword:
        keyword_query = [
            {field: {"$regex": keyword, "$options": "i"}}  # Case-insensitive regex search
            for field in all_fields
        ]
        query["$or"] = keyword_query
        cursor = request.app.database[candidate_collection].find(query)
        if cursor.retrieved == 0:
            raise CandidateDoesNotExist

        else:
            candidates = []
            for document in cursor:
                document["_id"] = str(document["_id"])
                candidates.append(document)

            return jsonable_encoder(candidates)


def export_to_csv(data, filename):
    with io.StringIO() as csv_buffer:
        writer = csv.DictWriter(csv_buffer, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

        with open(filename, 'w', newline='') as file:
            file.write(csv_buffer.getvalue())


def generate_report(request):
    data = list(request.app.database[candidate_collection].find())
    filename = "candidates_report.csv"
    export_to_csv(data, filename)
    response = StreamingResponse(
        content=open(filename, "rb"),
        media_type="application/octet-stream"
    )
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response
