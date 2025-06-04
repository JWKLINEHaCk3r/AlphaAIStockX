from fastapi import FastAPI
from backend.routes import credit_line

app = FastAPI()

app.include_router(credit_line.router)
