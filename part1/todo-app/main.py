import urllib.request
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# http://localhost/public/image.jpg
app.mount("/static", StaticFiles(directory="static"), name="static")
urllib.request.urlretrieve("https://picsum.photos/400/300", "/app/static/image.jpg")

templates = Jinja2Templates(directory="templates")


# http://localhost/
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"todo": "nothing", "request": request})

@app.post("/add")
def add(request: Request, todo: str = Form(...)):
    return templates.TemplateResponse("index.html", {"todo": todo, "request": request})
