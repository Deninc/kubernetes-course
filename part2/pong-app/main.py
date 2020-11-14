from fastapi import FastAPI

app = FastAPI()

app.counter = 0
with open("/tmp/pong_count.txt", "w") as f:
        f.write("0")

@app.get("/")
def read_root():
    app.counter += 1
    with open("/tmp/pong_count.txt", "w") as f:
        f.write(str(app.counter))
    return f"pong {app.counter}"
