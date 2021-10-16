from typing import Dict
from fastapi import FastAPI, Query
from pydantic import BaseModel
from manager.method_handler import MethodHandler

app = FastAPI()
method_handler = MethodHandler()


# Create the input class
class CreateCard(BaseModel):
    text: str = Query(None, min_length=1, max_length=50, regex="^[a-zA-ZñáéíóúÁÉÍÓÚ\s']+$")
    desk_name: str = Query(None, min_length=3, max_length=50, regex="^[a-zA-Z]+(:{2}[a-zA-Z]+)?$")
    language: str = Query(None, min_length=2, max_length=2, regex="^(es|en)$")
    ipa_shape: str = Query(None, min_length=2, max_length=10, regex="^(cmu|lexico)$")
    recipe: Dict[str, bool]


# Create an api root
@app.get("/")
def read_root():
    return {"status": "OK"}


# Create a card in Anki
@app.post("/create_card")
def create_card(params: CreateCard):
    parameters = {
        'text': params.text,
        'desk_name': params.desk_name,
        'language': params.language,
        'ipa_shape': params.ipa_shape
    }
    response = method_handler.detect_modules(parameters, params.recipe)
    return response
