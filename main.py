from typing import Union, Annotated

from fastapi import FastAPI, Depends

from pydantic import BaseModel

import shortuuid


app = FastAPI()
urlDict = dict()

@app.get("/")
async def root():
    return {"message": "Hello World"}


def uuid_maker(x):
    link = x
    pre = "127.0.0.1:8000/"
    uuid = shortuuid.ShortUUID().random(length=5)
    shorter = pre + uuid
    urlDict[shorter] = link
    return {
        
    "short-url":shorter, 
    "link": link
    
    }


def item(url: str):
    return uuid_maker(url)


@app.post("/shortie/{url}")
async def short_url(shortie: Annotated[dict, Depends(item)]):
    return shortie

