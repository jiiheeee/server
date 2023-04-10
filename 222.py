from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    data = request.args
    print("누가 자꾸 들어와", datetime.now())
    if int(data["value"]) == 0:
        return "0으로는 나눌 수 없습니다"
    return str(24//int(data["value"]))

@app.route('/main')
def main():
    return 'main page'
app.run(host='0.0.0.0', port=3001)