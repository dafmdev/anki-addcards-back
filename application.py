from typing import Dict
from fastapi import FastAPI, Query, Request
from pydantic import BaseModel
from manager.method_handler import MethodHandler
from manager.utils.run_bash import create_environment_variables

app = FastAPI()
method_handler = MethodHandler()


# Create the input class
class CreateCard(BaseModel):
    text: str = Query(None, min_length=1, max_length=50, regex="^[a-zA-ZñáéíóúÁÉÍÓÚ\!\?\,\.\;\s']+$")
    language: str = Query(None, min_length=2, max_length=2, regex="^(es|en)$")
    config: Dict[str, bool]


# Create an api root
@app.get("/")
def read_root():
    return {"status": "OK"}


# Create a card in Anki
@app.post("/create_card")
def create_card(params: CreateCard, request: Request):

    AWS_KEY = {'ACCESS_KEY': request.headers.get('ACCESS_KEY'), 'SECRET_KEY': request.headers.get('SECRET_KEY'),
               'REGION_NAME': request.headers.get('REGION_NAME'), 'BUCKETS_NAME': request.headers.get('BUCKETS_NAME')}
    create_environment_variables(AWS_KEY)

    parameters = {
        'text': params.text,
        'language': params.language
    }
    response = method_handler.detect_modules(parameters, params.config)

    return response
