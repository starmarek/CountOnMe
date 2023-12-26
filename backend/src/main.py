from fastapi import FastAPI

from .api.router import api_router

app = FastAPI()
app.include_router(api_router)
