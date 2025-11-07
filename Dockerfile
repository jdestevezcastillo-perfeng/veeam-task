FROM python:3.10-slim

WORKDIR /app

RUN pip3 install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY locustfile.py .

ENTRYPOINT ["poetry", "run", "locust"]