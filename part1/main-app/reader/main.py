import hashlib
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("/tmp/random_string.txt") as f:
        s = f.readline().rstrip()
    with open("/tmp/pong_count.txt") as f:
        c = f.readline().rstrip()
    h = hashlib.sha224(s.encode("utf-8")).hexdigest()
    return f"""
    <html>
        <head>
            <title>Main app</title>
        </head>
        <body>
            <p>{s} {h}</p>
            <p>Ping / Pongs: {c}</p>
        </body>
    </html>
    """
