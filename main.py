from typing import Union, Annotated

from fastapi import FastAPI, Depends

from fastapi.responses import RedirectResponse

from pydantic import BaseModel

import shortuuid


app = FastAPI()
url_list = {
    "uuid": "https://typer.tiangolo.com"
}

@app.get("/")
async def root():
    return {"message": "Hello World"}


def make_url(user_url):
    pre = "127.0.0.1:8000/"
    url_list[shorter] = user_url
    return {
        
    "short-url":(pre + (shortuuid.ShortUUID().random(length=5))) , 
    "link": user_url
    
    }


def item(url: str):
    return make_url(url)


@app.post("/shortie/{url}")
async def short_url(shortie: Annotated[dict, Depends(item)]):
    return shortie

@app.get("/get/{uuid}")
def get_url(uuid: str):
    print(url_list)
    if uuid in url_list:
        return RedirectResponse(
            url = (url_list[uuid])
            )
