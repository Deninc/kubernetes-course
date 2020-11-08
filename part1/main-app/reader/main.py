import hashlib
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    with open("/tmp/random_string.txt") as f:
        s = f.readline().rstrip()
    h = hashlib.sha224(s.encode("utf-8")).hexdigest()
    return s + h
