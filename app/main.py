# app/main.py
from fastapi import FastAPI
from .database import init_db
from .routers import user, course, quiz, forum, feedback

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(user.router)
app.include_router(course.router)
app.include_router(quiz.router)
app.include_router(forum.router)
app.include_router(feedback.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-Learning Platform!"}

