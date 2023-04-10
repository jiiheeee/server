from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    data = request.args
    print("사용자가 보내준 데이터")
    if data =="age":
        # 나이를 계산해서 어쩌구~
    elif data == "name":
        # db에서 이름을 조회해서 데이터로 응답
    return f'요청에 대한 응답: {data}'
app.run(host='0.0.0.0', port=81)