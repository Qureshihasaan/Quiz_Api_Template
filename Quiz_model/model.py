# from typing import Optional , List
# from datetime import datetime
# from pydantic import BaseModel


# class courses():
#     def __init__(self , course_id : int , course_name : str , ):
#         self.course_id = course_id
#         self.course_name = course_name
        
#         self.quizzes : List["Quiz"] = []
        
        
# class Topic():
#     def __init__(self , topic_id : int , topic_name : str ):
#         self.topic_id = topic_id
#         self.topic_name = topic_name
    
    


# class Quiz(BaseModel):
#     def __init__(self , quiz_id : int , course_id : int  , quiz_name : str , quiz_timelimit : Optional[datetime]):
#         self.quiz_id = quiz_id
#         self.course_id = course_id 
#         self.quiz_name = quiz_name
#         self.quiz_timelimit = quiz_timelimit
        
#         self.question : list["Questions"] = []
        
        
# class Questions():
#     def __init__(self, quiz_id : int , question_id : int , question_text : str , question_type : str):
#         self.quiz_id = quiz_id
#         self.question_id = question_id
#         self.question_text = question_text
#         self.question_type = question_type
        
        
# class free_text_question(Questions):
#     def __init__(self, quiz_id : int, question_id : int, question_text : str , correct_answer : str):
#         super().__init__(quiz_id, question_id, "free_text" , question_text,)
#         self.correct_answer = correct_answer
        
        
# class coding_question(Questions):
#     def __init__(self, quiz_id : int, question_id : int, question_text : str, correct_answer : str):
#         super().__init__(quiz_id, question_id, "coding" , question_text,)
#         self.correct_answer = correct_answer