from fastapi import FastAPI
from app.routes import chat

app = FastAPI(title="Customer AI System")

app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "System running"}