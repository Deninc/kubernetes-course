import os
import hashlib
import urllib.request
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("/tmp/random_string.txt") as f:
        s = f.readline().rstrip()
    c = urllib.request.urlopen("http://pong-svc:1234/count").read()
    h = hashlib.sha224(s.encode("utf-8")).hexdigest()
    return f"""
    <html>
        <head>
            <title>Main app</title>
        </head>
        <body>
            <p>{os.environ["MESSAGE"]}</p>
            <p>{s} {h}</p>
            <p>Ping / Pongs: {c}</p>
        </body>
    </html>
    """
