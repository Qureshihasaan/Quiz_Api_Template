from Quiz_model.model_sql import courses
from fastapi import FastAPI
from sqlmodel import Session
from Database.database import engine

app : FastAPI = FastAPI()


@app.post("/courses")
def create_courses(question : courses):
    with Session(engine) as session:
        session.add(courses)
        session.commit()
        session.refresh(courses)
        return courses