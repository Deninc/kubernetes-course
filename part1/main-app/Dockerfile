FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8

WORKDIR /app

COPY main.py print_string.sh ./

CMD ./print_string.sh & /start.sh
