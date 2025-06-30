from fastapi import FastAPI
from app.adapters.fastapi_controller import router

app = FastAPI()
app.include_router(router)
