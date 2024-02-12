# from fastapi import FastAPI
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from model import Quiz
# from database import engine


from fastapi import FastAPI
from sqlmodel import Session
from Database.database import engine
from Quiz_model.model_sql import Quizess



app : FastAPI = FastAPI()


# def get_db():
#     yield Session
    
    
# @app.get("/")
# def read_quiz():
#     return {"Hello": "World"}

@app.post("/Quiz")
def create_quiz(quiz: Quizess):
    with Session(engine) as session:
        session.add(quiz)
        session.commit()
        session.refresh(quiz)
        return quiz  