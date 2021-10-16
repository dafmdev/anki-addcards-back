from typing import Optional, List, Dict
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CreateCard(BaseModel):
    word: str
    language: str = "en"
    desk_name: str

@app.get("/")
def read_root():
    return {"status": "OK"}

@app.post("/create_card")
def create_card(params: CreateCard):
    parameters = {
        'word': params.word,
        'language': params.language,
        'desk_name': params.desk_name
    }
    response = parameters
    return response