from fastapi import FastAPI, dependencies, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

import models, schemas

from database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI(title= 'API Catalago de Filmes')
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return{'mensagem':'Welcome to the jungle'}