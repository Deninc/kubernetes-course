import os
import psycopg2
import urllib.request
from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# http://localhost/static/image.jpg
app.mount("/static", StaticFiles(directory="static"), name="static")
urllib.request.urlretrieve("https://picsum.photos/400/300", "/app/static/image.jpg")

templates = Jinja2Templates(directory="templates")

conn = psycopg2.connect(host="pg-svc", dbname="postgres", user="postgres", password=os.environ["POSTGRES_PASSWORD"])

# https://www.psycopg.org/docs/usage.html#with-statement
with conn:
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS todos (id serial PRIMARY KEY, todo varchar);")

@app.get("/todos")
def read_root(request: Request):
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT todo FROM todos")
            todos = [x[0] for x in cur.fetchall()]

    return templates.TemplateResponse("index.html", {"todos": todos, "request": request})

@app.post("/todos")
def add(todo: str = Form(...)):
    ### ... means todo param is required
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO todos(todo) VALUES ('{todo}')")

    return RedirectResponse("/todos", status_code=status.HTTP_303_SEE_OTHER)