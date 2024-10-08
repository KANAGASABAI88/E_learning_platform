# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: str

class User(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    title: str
    description: str

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    instructor_id: int
    materials: List[str] = []

    class Config:
        orm_mode = True

class MaterialBase(BaseModel):
    file_path: str

class MaterialCreate(MaterialBase):
    course_id: int

class QuizBase(BaseModel):
    question: str

class QuizCreate(QuizBase):
    course_id: int

class ForumPostBase(BaseModel):
    content: str

class ForumPostCreate(ForumPostBase):
    user_id: int

class FeedbackBase(BaseModel):
    content: str

class FeedbackCreate(FeedbackBase):
    user_id: int
    course_id: int

