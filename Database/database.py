# from sqlalchemy import create_engine 
# from sqlalchemy.orm import Session
# from sqlalchemy.ext.declarative import declarative_base
# from model_sql import create_quiz

from sqlmodel import SQLModel , create_engine , Field


database_url = "postgresql://hasaanqureshi150:PuTJD6wSd1Rt@ep-long-rice-a5p9vpav.us-east-2.aws.neon.tech/Fast_api_quiz_template?sslmode=require"

engine = create_engine(database_url , echo = True)


# Base = declarative_base


# def create_db_tables():
#     Base.metadata.create_all(engine)
    
def create_db_tables():
    SQLModel.metadata.create_all(engine)
    
if __name__ == "__main__":
    create_db_tables()
    
