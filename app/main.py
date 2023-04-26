from fastapi import FastAPI

anantTube_api = FastAPI()


@anantTube_api.get('/')
def home():
    return {"greetings": "Hello, world!"}
