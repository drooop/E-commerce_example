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
                               'meta': {'msg': 'success', 'status': 200}})
        else:
            return json.dumps({'meta': {'msg': 'fail to login', 'status': 400}})
    else:
        return json.dumps({'data': 'method error'})


@app.route('/api/menus', methods=['GET'])
def getMenu():
    menuList = {
        'data': [
            {
                'id': 1,
                'authName': '用户管理',
                'path': 'null',
                'children': [
                    {
                        'id': 11,
                        'authName': '用户列表',
                        'path': 'users',
                    }
                ]
            },
            {
                'id': 2,
                'authName': '权限管理',
                'path': 'null',
                'children': [
                    {
                        'id': 21,
                        'authName': '角色列表',
                        'path': 'roles',
                    },
                    {
                        'id': 22,
                        'authName': '权限列表',
                        'path': 'rights',
                    }
                ]
            },
            {
                'id': 3,
                'authName': '商品管理',
                'path': 'null',
                'children': [
                    {
                        'id': 31,
                        'authName': '商品列表',
                        'path': 'null',
                    },
                    {
                        'id': 32,
                        'authName': '分类参数',
                        'path': 'null',
                    },
                    {
                        'id': 33,
                        'authName': '商品分类',
                        'path': 'null',
                    }
                ]
            },
            {
                'id': 4,
                'authName': '订单管理',
                'path': 'null',
                'children': [
                    {
                        'id': 41,
                        'authName': '订单列表',
                        'path': 'null',
                    },
                    {
                        'id': 42,
                        'authName': '订单列表2',
                        'path': 'null',
                    }

                ]
            },
            {
                'id': 5,
                'authName': '数据统计',
                'path': 'null',
                'children': [
                    {
                        'id': 51,
                        'authName': '数据1',
                        'path': 'null',
                    },
                    {
                        'id': 52,
                        'authName': '数据2',
                        'path': 'null',
                    }
                ]
            }
        ],
        'meta': {
            'msg': '获取菜单列表成功',
            'status': 200
        }
    }
    return json.dumps(menuList)


@app.route('/api/users', methods=['GET'])
def getUsers():
    testData = {
        'data': {
            'pagenum': 1,
            'total': 10,
            'users': [
                {
                    'id': 500,
                    'role_name': "超级管理员",
                    'user_name': 'admin',
                    'create_time': '1486720211',
                    'mobile': '13950068590',
                    'email': 'linken@qq.com',
                    'mg_state': True
                },
                {
                    'id': 400,
                    'role_name': "测试角色0",
                    'user_name': 'linken0',
                    'create_time': '1486720211',
                    'mobile': '13950068591',
                    'email': 'linken0@qq.com',
                    'mg_state': False
                },
                {
                    'id': 401,
                    'role_name': "测试角色1",
                    'user_name': 'linken1',
                    'create_time': '1486720211',
                    'mobile': '13950068591',
                    'email': 'linken1@qq.com',
                    'mg_state': False
                },
                {
                    'id': 402,
                    'role_name': "测试角色2",
                    'user_name': 'linken2',
                    'create_time': '1486720211',
                    'mobile': '13950068591',
                    'email': 'linken2@qq.com',
                    'mg_state': False
                },
                {
                    'id': 403,
                    'role_name': "测试角色3",
                    'user_name': 'linken3',
                    'create_time': '1486720211',
                    'mobile': '13950068591',
                    'email': 'linken3@qq.com',
                    'mg_state': False
                },
                {
                    'id': 404,
                    'role_name': "测试角色4",
                    'user_name': 'linken4',
                    'create_time': '1486720211',
                    'mobile': '13950068591',
                    'email': 'linken4@qq.com',
                    'mg_state': False
                },
                {
                    'id': 405,
                    'role_name': "测试角色5",
                    'user_name': 'linken5',
                    'create_time': '1486720211',
                    'mobile': '13950068591',
                    'email': 'linken5@qq.com',
                    'mg_state': False
                },
                {
                    'id': 406,
                    'role_name': "测试角色6",
                    'user_name': 'linken6',
                    'create_time': '1486720211',
                    'mobile': '13950068591',
                    'email': 'linken6@qq.com',
                    'mg_state': False
                },
                {
                    'id': 407,
                    'role_name': "测试角色7",
                    'user_name': 'linken7',
                    'create_time': '1486720211',
                    'mobile': '13950068591',
                    'email': 'linken7@qq.com',
                    'mg_state': False
                },
                {
                    'id': 408,
                    'role_name': "测试角色8",
                    'user_name': 'linken8',
                    'create_time': '1486720211',
                    'mobile': '13950068591',
                    'email': 'linken8@qq.com',
                    'mg_state': False
                }
            ]
        },
        'meta': {
            'msg': '获取管理员列表成功',
            'status': 200
        }
    }
    return json.dumps(testData)

if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(host='0.0.0.0', port=80, debug=True)
