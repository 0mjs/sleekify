from sleekify import Sleekify, Guard
from pydantic import BaseModel
from typing import Optional

app = Sleekify()


async def Authenticate(with_token: bool = False):
    if with_token:
        return {"user": "Matt", "token": "123456"}
    return {"user": "Matt"}


@app.post("/secure")
async def secure(auth=Guard(Authenticate, with_token=True)):
    return {"message": "success", "auth": auth}


@app.get("/get-item")
async def get():
    return {"data": "item-1"}


class ItemModel(BaseModel):
    name: str
    price: Optional[int] = None


@app.post("/create-item")
async def create(item: ItemModel):
    return {"data": f"item-{item.name}"}
