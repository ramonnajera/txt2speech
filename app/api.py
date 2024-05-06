from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/css", StaticFiles(directory="src/css"), name="css")
app.mount("/imagenes", StaticFiles(directory="src/img"), name="img")
app.mount("/js", StaticFiles(directory="src/js"), name="js")

templates = Jinja2Templates(directory="src/templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("page/home.html", {"request": request})
