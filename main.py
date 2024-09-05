from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), "static")
templates = Jinja2Templates(directory="templates")

class WebPage:
    footer = "@REF Marketing 2024"

@app.get("/")
async def home(request: Request):
    context = {
        "request":request,
        "title": "REF MARKETING",
        "logo_title1":"REF",
        "logo_title2":"Marketing",
        "web":WebPage
    }
    return templates.TemplateResponse("index.html", context)

@app.get("/base")
async def base(request: Request):
    context = {
        "request":request,
        "title": "REF MARKETING",
        "logo_title1":"REF",
        "logo_title2":"Marketing",
        "web":WebPage
    }
    return templates.TemplateResponse("admin2/blank.html", context)

@app.get("/login")
async def login(request: Request):
    context = {
        "request":request,
        "title": "REF MARKETING",
        "logo_title1":"REF",
        "logo_title2":"Marketing",
        "web":WebPage
    }
    return templates.TemplateResponse("admin2/login.html", context)