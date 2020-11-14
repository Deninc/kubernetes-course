from fastapi import FastAPI

app = FastAPI()

# many app.counter is handled separately by processes => write to file as cache
# https://github.com/tiangolo/fastapi/issues/592
with open("/tmp/pong_count.txt", "w") as f:
        f.write("0")

@app.get("/")
def read_root():
    with open("/tmp/pong_count.txt") as f:
        c = int(f.readline().rstrip())
    c += 1
    with open("/tmp/pong_count.txt", "w") as f:
        f.write(str(c))
    return f"pong {c}"

@app.get("/count")
def read_count():
    with open("/tmp/pong_count.txt") as f:
        c = int(f.readline().rstrip())
    return c
