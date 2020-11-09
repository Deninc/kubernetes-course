import urllib.request
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# http://localhost/public/image.jpg
app.mount("/public", StaticFiles(directory="public"), name="public")
urllib.request.urlretrieve("https://picsum.photos/400/300", "/app/public/image.jpg")

# http://localhost/
@app.get("/")
def read_root():
    return FileResponse('public/index.html')
