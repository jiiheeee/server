from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def name():
    data=request.args
    return '안녕하세요.'+data['value']+'님'
app.run(host='0.0.0.0', port=83)