<script>
  let message; //message라는 변수 생성

  fetch("http://127.0.0.1:8000/hello").then((response)=>{ 
    response.json().then((json)=>{ //FastAPI의 hello API를 호출하여 돌려 받은 값을
      message = json.message; // message변수에 넣기
    });
  });
</script>

<h1>{message}</h1>