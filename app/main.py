from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from app import models, routes
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(routes.router, tags=["MortgageCalculator"], prefix="/api/v1")


@app.get("/api/healthchecker")
def root():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    msg = f"💪🏆🎉 The API is LIVE with latest version of FastAPI! {now}"
    return {"message": msg}
