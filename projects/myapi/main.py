from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import  question_router #파일에 생성한 라우터 객체를 앱에 등록

app=FastAPI()

origins = [
    "http://127.0.0.1:5173", # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello") #/hello라는 URL요청이 발생하면
# def hello():       # 해당함수를 실행하여 결과를 리턴하라는 의미
#     return{"message" : "안녕하세요 화이보"}

app.include_router(question_router.router)#include 메소드 사용하여 라우터 객체 등록