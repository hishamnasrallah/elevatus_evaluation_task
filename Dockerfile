FROM python:3.10-slim

RUN apt-get update && apt-get upgrade -y
RUN pip install poetry
WORKDIR /app
COPY  pyproject.toml /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction
COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
