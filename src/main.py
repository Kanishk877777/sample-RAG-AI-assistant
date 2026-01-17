from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="Legal Assistant")
app.include_router(router)
