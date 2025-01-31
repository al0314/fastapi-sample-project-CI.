
from fastapi import FastAPI
from . import db  
from . import redis  

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Application has started!")
    print(f"MongoDB connected to {db.name}")  

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
