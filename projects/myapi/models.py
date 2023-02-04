from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Question(Base):
    __tablename__ = "question" #테이블 이름

    id = Column(Integer, primary_key=True) #번호, Primary Key
    subject = Column(String, nullable=False) #제목
    content = Column(Text, nullable=False) #내용
    create_date = Column(DateTime, nullable=False) #작성일시
    #Column(데이터 타입,null을 사용할지)

class Answer(Base):
    __tablename__="answer"

    id = Column(Integer, primary_key=True) #Primary Key
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id")) #ForeignKey, 답을 질문과 연결하기 위한 키
    question = relationship("Question", backref="answers")
