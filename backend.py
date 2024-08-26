from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from API import Security

app = FastAPI(root_path="/api/")

@app.get("/test/{item_id}")
async def test(item_id:str):
    return {"hello": item_id}
