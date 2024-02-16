from fastapi import FastAPI

from fastapi.responses import RedirectResponse

from pydantic import BaseModel, HttpUrl

import shortuuid


app = FastAPI()
url_list = {
    "uuid": "https://typer.tiangolo.com"
}

@app.get("/")
async def root():
    return {"message": "Hello World"}

class Item(BaseModel):
    url: HttpUrl

@app.post("/shortie/{user_url.url}")
async def short_url(user_url: Item):
 
    short_url = (shortuuid.ShortUUID().random(length=5))
    url_list[short_url] = user_url.url
    return {
        
    "short-url":short_url , 
    "link": user_url.url
    }


@app.get("/get/{uuid}")
def get_url(uuid: str):
    if uuid in url_list:
        return RedirectResponse(
            url = (url_list[uuid])
            )

@app.get("/readdictionary")
def read_dictionary():
    return url_list