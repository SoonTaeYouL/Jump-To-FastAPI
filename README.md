# Jump-To-FastAPI
----------------------------------------------
Project Structure

├── main.py        안에 app객체(핵심)을 통해 FastAPI 설정, 전체적인 환경 설정

├── database.py   데이터베이스 설정

├── models.py     모델 클래스들을 정의할 파일

├── domain        질문과 답변을 작성하는 게시판

│   ├── answer

│   ├── question

│   └── user

└── frontend       소스 및 빌드 파일들을 저장할 루트 디렉터리
