import validators
from fastapi import FastAPI, status, HTTPException

from . import schemas

app = FastAPI()

def raise_bad_request(message):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)

@app.get('/')
def read_root() -> dict:
    return {
        'message' : 'Server running successfully!',
        'status' : status.HTTP_200_OK
    }


@app.post('/url')
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request(message='Your provided URL is not valid!')
    return {
        'status' : status.HTTP_201_CREATED,
        'message' : f'TODO: Create URL database entry {url.target_url}'
    }