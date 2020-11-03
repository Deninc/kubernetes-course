import uuid
import logging
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()
with open("random_string.txt") as f:
    random_s = f.read()

@app.get("/")
def read_root():
    return random_s
