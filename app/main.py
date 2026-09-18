
from fastapi import FastAPI
from app.routers.menu import router

app = FastAPI(title="WAD Individu Menu API")
app.include_router(router)

@app.get("/")
def root():
    return {"message":"API Running"}

@app.get("/health")
def health():
    return {"status":"ok"}
