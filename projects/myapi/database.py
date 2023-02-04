from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"
#데이터베이스 접속주소 = sqlite3데이터베이스의 파일을 프로젝트 루트 디렉터리에 저장

engine = create_engine(#컨넥션 풀(데이터베이스에 접속하는 객체를 일정 갯수만큼 만들어 놓고 돌려가며 사용하는 것)
    #컨넥션 풀을 생성(접속 세션수 제어, 접속에 소요되는 시간을 줄이고자)
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)#SessionLocal은 데이터베이스 접속을 위한 클래스
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#autocommit=True: commit 사인없이도 즉시 데이터베이스에 변경사항이 적용됨
#autocommit=False: commit이라는 싸인이 있어야 데이터베이스 저장(rollback도 가능)
Base = declarative_base()#데이터베이스 모델 구성할때 사용