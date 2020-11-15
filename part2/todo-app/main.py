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


# http://localhost/
@app.get("/todos")
def read_root(request: Request):
    try:
        with open("/tmp/list.txt") as f:
                todos = f.read().splitlines()
    except FileNotFoundError:
        todos = []

    return templates.TemplateResponse("index.html", {"todos": todos, "request": request})

@app.post("/todos")
def add(todo: str = Form(...)):
    ### ... means todo param is required
    with open("/tmp/list.txt", "a") as f:
        f.write(todo + "\n")

    return RedirectResponse("/todos", status_code=status.HTTP_303_SEE_OTHER)
