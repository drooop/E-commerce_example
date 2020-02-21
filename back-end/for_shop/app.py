from flask import Flask
from flask_cors import CORS
from flask import request
import json


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        data = request.get_data().decode('utf-8')
        data_dict = json.loads(data)
        print(data_dict)
        if data_dict.get('username') == 'drop' and data_dict.get('password') == '123321123':
            return json.dumps({'data': {'token': 'test_token 123321123'},
            'meta': {'msg': 'success', 'status':200}})
        else:
            return json.dumps({'meta': {'msg': 'fail to login', 'status':400}})
    else:
        return json.dumps({'data': 'method error'})


if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run(host='0.0.0.0', port=80, debug=True)
