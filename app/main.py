from fastapi import FastAPI, HTTPException
from app import models, schemas, crud, database

app = FastAPI()

@app.on_event("startup")
async def startup():
        await database.init_db()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Fashion Store API!"}

@app.get("/categories/{category_name}", response_model=list[schemas.Item])
async def get_category(category_name: str):
    items = await crud.get_category_items(category_name)
    if not items:
           raise HTTPException(status_code=404, detail="Category not found")
    return items

@app.post("/categories/{category_name}", response_model=schemas.Item)
async def create_item(category_name: str, item: schemas.ItemCreate):
       return await crud.create_item(category_name, item)

