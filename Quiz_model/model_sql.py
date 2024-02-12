from sqlmodel import SQLModel , Field 
from datetime import datetime
from typing import Optional
from typing import Union

class courses(SQLModel , table = True):
    course_id : int= Field(default = None , primary_key = True)
    course_name : str = Field(default = None)
    
    
class Topics(SQLModel , table = True):
    topic_id : int = Field(default = None, primary_key = True)
    topic_name : str = Field(default = None)
    course_id : int= Field(default = None, foreign_key = "courses.course_id")
    
    
class Quizess(SQLModel , table = True ):
    quiz_id : int= Field(default = None, primary_key= True)
    quiz_name : str = Field(default = None)
    quiz_timelimt : Optional[datetime] = None
    course_id : int= Field(default = None , foreign_key = "courses.course_id")
    topic_id :int= Field(default = None , foreign_key = "Topics.topic_id")
    
class Questions(SQLModel , table = True):
    quiz_id : int = Field(default = None , foreign_key = "Quizess.quiz_id")
    question_id : int= Field(default = None, primary_key = True)
    question_text : str = Field(default = None)
    
    
class Free_type_question(Questions):
    correct_answer : str 

class coding_question(Questions):
    correct_answer : str     

class single_Mcqs_Question(Questions):
    correct_answer : str 