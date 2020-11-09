FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8

WORKDIR /app
RUN pip install aiofiles

COPY main.py .
COPY public public
