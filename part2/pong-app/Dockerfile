FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim


WORKDIR /app
RUN pip install psycopg2-binary

COPY main.py .
