from fastapi import APIRouter
from model import click

router = APIRouter(prefix="/log")

test_list = []

#post
@router.post("/test")
async def add_hello(test: click):
    test_list.append(test)
    return {
        'message': 'add success!'
    }
    
@router.get("/test")
async def retrieve_hello():
    return {
        'test': test_list
    }

#path parameter
@router.get("/test/{click}")
async def get_click(click: str):
    for test in test_list:
        if test.id == click:
            return {
                "test": "path parameter"
            }
    return {
        "message": "test with supplied ID doesn't exist."
    }