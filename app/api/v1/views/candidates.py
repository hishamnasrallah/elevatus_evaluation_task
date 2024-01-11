from fastapi import APIRouter, Body, Request, status, Query, Depends
from app.api.repositories import candidates
from app.api.v1.dependancies.authorization import validate_authorization
from app.api.v1.serializers.candidates import CandidateBasicSerializer, CandidateResponseSerializer
from utils.http_response import http_response
from core.constants.response_messages import ResponseConstants

router = APIRouter(
    prefix='/v1',
    tags=[]
)


@router.post("/create/", response_model=CandidateResponseSerializer)
def create_candidate(request: Request, request_body: CandidateBasicSerializer = Body(...),
                     token=Depends(validate_authorization)):
    data = candidates.create_candidate(request_body, request)
    print(data)
    return http_response(data=data, status=status.HTTP_201_CREATED,
                         message=ResponseConstants.CREATED_MSG)


@router.get("/all/", response_model=CandidateResponseSerializer)
def all_candidates(request: Request, token=Depends(validate_authorization)):
    data = candidates.get_candidates(request)
    return http_response(data=data, request=request, status=status.HTTP_200_OK,
                         message=ResponseConstants.RETRIEVED_MSG)


@router.get("/filter/", response_model=CandidateResponseSerializer)
def get_filtered_candidates(request: Request,
                       keyword: str = Query(None, title="Global Search Keyword",
                                            description="Search across all fields"),
                       token=Depends(validate_authorization)):
    data = candidates.get_candidate_filter(keyword, request)

    return http_response(data=data, request=request, status=status.HTTP_200_OK,
                         message=ResponseConstants.RETRIEVED_MSG)


@router.get("/{candidate_id}/", response_model=CandidateResponseSerializer)
def get_candidate(request: Request, candidate_id: str, token=Depends(validate_authorization)):
    print(candidate_id)
    data = candidates.get_candidate(candidate_id, request)
    return http_response(data=data, status=status.HTTP_200_OK,
                         message=ResponseConstants.RETRIEVED_MSG)


@router.put("/{candidate_id}/", response_model=CandidateResponseSerializer)
def update_candidate(candidate_id: str, request: Request, request_body: CandidateBasicSerializer = Body(...),
                     token=Depends(validate_authorization)):
    data = candidates.update_candidate(candidate_id, request_body, request)
    return http_response(data=data, status=status.HTTP_200_OK,
                         message=ResponseConstants.UPDATED_MSG)


@router.delete("/{candidate_id}/", response_model=CandidateResponseSerializer)
def delete_candidate(candidate_id: str, request: Request, token=Depends(validate_authorization)):
    data = candidates.delete_candidate(candidate_id, request)
    return http_response(data=data, status=status.HTTP_200_OK,
                         message=ResponseConstants.DELETED_MSG)


@router.get("/generate-report")
def export_csv(request: Request, token=Depends(validate_authorization)):
    data = candidates.generate_report(request)
    return data
