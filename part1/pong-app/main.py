from fastapi import FastAPI

app = FastAPI()

app.counter = 0

@app.get("/")
def read_root():
    app.counter += 1
    return f"pong {app.counter}"
