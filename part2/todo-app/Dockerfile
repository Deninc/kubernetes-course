FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

WORKDIR /app
RUN pip install aiofiles python-multipart jinja2 psycopg2-binary

COPY . .
