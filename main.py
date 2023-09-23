from fastapi import FastAPI
from router import router
from model import click

app = FastAPI()

@app.get('/')
async def hello():
    return {'message' : 'test'}

app.include_router(router)

