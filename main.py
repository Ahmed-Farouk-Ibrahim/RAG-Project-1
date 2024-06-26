from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env")

# From directory routes reach base.py file to call base_router decorator
from routes import base

app = FastAPI()

app.include_router(base.base_router)
