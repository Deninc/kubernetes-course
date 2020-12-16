FROM python:3.8-slim

WORKDIR /app
RUN pip install requests asyncio-nats-client

COPY . .

CMD ["python", "./broadcaster.py"]
