from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import crud
from db import SessionLocal
from model import Daily

app = FastAPI()

origins = ["http://localhost:8080", "http://localhost:5175"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    d = SessionLocal()
    try:
        yield d
    finally:
        d.close()


@app.get("/")
def root():
    return {"Hello", "World"}


@app.get("/api/Daily/GetAll", response_model=List[Daily])
def get_all(session: Session = Depends(get_db)):
    return crud.get_all(session)


@app.get("/api/Daily/Get", response_model=Daily, responses={400: {"model": str}})
def get(id: int, session: Session = Depends(get_db)):
    return crud.get(session, id)


@app.post("/api/Daily/Add", responses={400: {"model": str}})
def add(daily: Daily, session: Session = Depends(get_db)):
    return crud.add(session, daily)


@app.post("/api/Daily/Update", responses={400: {"model": str}})
def update(daily: Daily, session: Session = Depends(get_db)):
    return crud.update(session, daily)


@app.post("/api/Daily/Remove")
def remove(daily: Daily, session: Session = Depends(get_db)):
    return crud.remove(session, daily)
