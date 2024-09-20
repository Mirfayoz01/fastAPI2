from fastapi import FastAPI

app = FastAPI()

data = {
    "Id" : 1,
    "UserId" : 1,
    "title" : "Hello",
    "body" : "My FastAPI"
}

@app.get("/")
async def book():
    return {"name": "Hello world"}


@app.get("/item/{item_id}")
async def items(item_id: int):
    return {"item_id": item_id}


@app.get("/book")
async def datas():
    return data

@app.get("/name/{item_name}")
async def name(item_name: str):
    if item_name.isnumeric():
        raise HTTPException(status_code=404, detail="Item not found")
    return {"Hello": item_name}


@app.post("/book/")
async def create_book(book: book):
    return {"book": book}
    