from flask import Flask
from flask_cors import CORS
from flask import request
import json


app = Flask(__name__)
CORS(app)

userIdBase = 408

menuList = [
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
]

userList = [
    {
        'id': 500,
        'role_name': "超级管理员",
        'username': 'admin',
        'create_time': '1486720211',
        'mobile': '13950068590',
        'email': 'linken@qq.com',
        'mg_state': True
    },
    {
        'id': 400,
        'role_name': "测试角色0",
        'username': 'linken0',
        'create_time': '1486720211',
        'mobile': '13950068591',
        'email': 'linken0@qq.com',
        'mg_state': False
    },
    {
        'id': 401,
        'role_name': "测试角色1",
        'username': 'linken1',
        'create_time': '1486720211',
        'mobile': '13950068591',
        'email': 'linken1@qq.com',
        'mg_state': False
    },
    {
        'id': 402,
        'role_name': "测试角色2",
        'username': 'linken2',
        'create_time': '1486720211',
        'mobile': '13950068591',
        'email': 'linken2@qq.com',
        'mg_state': False
    },
    {
        'id': 403,
        'role_name': "测试角色3",
        'username': 'linken3',
        'create_time': '1486720211',
        'mobile': '13950068591',
        'email': 'linken3@qq.com',
        'mg_state': False
    },
    {
        'id': 404,
        'role_name': "测试角色4",
        'username': 'linken4',
        'create_time': '1486720211',
        'mobile': '13950068591',
        'email': 'linken4@qq.com',
        'mg_state': False
    },
    {
        'id': 405,
        'role_name': "测试角色5",
        'username': 'linken5',
        'create_time': '1486720211',
        'mobile': '13950068591',
        'email': 'linken5@qq.com',
        'mg_state': False
    },
    {
        'id': 406,
        'role_name': "测试角色6",
        'username': 'linken6',
        'create_time': '1486720211',
        'mobile': '13950068591',
        'email': 'linken6@qq.com',
        'mg_state': False
    },
    {
        'id': 407,
        'role_name': "测试角色7",
        'username': 'linken7',
        'create_time': '1486720211',
        'mobile': '13950068591',
        'email': 'linken7@qq.com',
        'mg_state': False
    },
    {
        'id': 408,
        'role_name': "测试角色8",
        'username': 'linken8',
        'create_time': '1486720211',
        'mobile': '13950068591',
        'email': 'linken8@qq.com',
        'mg_state': False
    }
]

rightsList = [
    {
        'id': 101,
        'authName': '模型管理',
        'level': '0',
        'pid': 0,
        'path': 'models'
    },
    {
        'id': 102,
        'authName': '订单管理',
        'level': '0',
        'pid': 1,
        'path': 'orders'
    },
    {
        'id': 103,
        'authName': '权限管理',
        'level': '0',
        'pid': 2,
        'path': 'rights'
    },
    {
        'id': 104,
        'authName': '模型列表',
        'level': '1',
        'pid': 3,
        'path': 'models'
    },
    {
        'id': 105,
        'authName': '添加模型',
        'level': '2',
        'pid': 3,
        'path': 'models'
    },
    {
        'id': 106,
        'authName': '订单列表',
        'level': '2',
        'pid': 1,
        'path': 'orders'
    },
    {
        'id': 107,
        'authName': '添加订单',
        'level': '3',
        'pid': 2,
        'path': 'orders'
    },
    {
        'id': 108,
        'authName': '用户列表',
        'level': '1',
        'pid': 3,
        'path': 'users'
    },
    {
        'id': 109,
        'authName': '角色列表',
        'level': '1',
        'pid': 3,
        'path': 'roles'
    },
    {
        'id': 110,
        'authName': '权限列表',
        'level': '1',
        'pid': 3,
        'path': 'rights'
    },
    {
        'id': 111,
        'authName': '分类参数',
        'level': '1',
        'pid': 3,
        'path': 'params'
    },
    {
        'id': 112,
        'authName': '模型修改',
        'level': '2',
        'pid': 3,
        'path': 'models'
    }
]

rightsTree = {
    'id': 1,
    'authName': '模型管理1',
    'level': '0',
    'pid': 0,
    'children': [
        {
            'id': 11,
            'authName': '模型管理1',
            'level': '0',
            'pid': 0,
            'children': [
                {
                    'id': 111,
                    'authName': '模型管理1',
                    'level': '0',
                    'pid': 0
                },
                {
                    'id': 112,
                    'authName': '模型管理1',
                    'level': '0',
                    'pid': 0
                },
            ]
        },
        {
            'id': 12,
            'authName': '模型管理1',
            'level': '0',
            'pid': 0
        },
    ]
},

rolesList = [
    {
        'id': 1,
        'roleName': '主管',
        'roleDesc': '技术负责人',
        'children': [
            {
                'id': 11,
                'authName': '模型管理',
                'path': 'null',
                'children': [
                    {
                        'id': 111,
                        'authName': '模型列表',
                        'path': 'null',
                        'children': [
                            {
                                'id': 1111,
                                'authName': '添加模型',
                                'path': 'null'
                            }
                        ]
                    }
                ]
            }
        ]
    },
        {
        'id': 2,
        'roleName': '测试角色',
        'roleDesc': '测试角色描述',
        'children': [
            {
                'id': 21,
                'authName': '模型管理',
                'path': 'null',
                'children': [
                    {
                        'id': 211,
                        'authName': '模型列表',
                        'path': 'null',
                        'children': [
                            {
                                'id': 2111,
                                'authName': '添加模型',
                                'path': 'null'
                            }
                        ]
                    }
                ]
            }
        ]
    },
        {
        'id': 3,
        'roleName': '测试角色2',
        'roleDesc': '测试角色描述2',
        'children': [
            {
                'id': 31,
                'authName': '模型管理',
                'path': 'null',
                'children': [
                    {
                        'id': 311,
                        'authName': '模型列表',
                        'path': 'null',
                        'children': [
                            {
                                'id': 3111,
                                'authName': '添加模型',
                                'path': 'null'
                            }
                        ]
                    }
                ]
            }
        ]
    },
        {
        'id': 4,
        'roleName': 'drop',
        'roleDesc': 'dropdrop',
        'children': [
            {
                'id': 41,
                'authName': '模型管理',
                'path': 'null',
                'children': [
                    {
                        'id': 411,
                        'authName': '模型列表',
                        'path': 'null',
                        'children': [
                            {
                                'id': 4111,
                                'authName': '添加模型',
                                'path': 'null'
                            }
                        ]
                    }
                ]
            }
        ]
    }
]


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
    menu = {
        'data': menuList,
        'meta': {
            'msg': '获取菜单列表成功',
            'status': 200
        }
    }
    return json.dumps(menu)


@app.route('/api/users', methods=['GET', 'POST'])
def getUsers():
    global userIdBase
    if request.method == "POST":
        newUser = request.get_data().decode('utf-8')
        newUser = json.loads(newUser)
        userIdBase += 1
        newUser['id'] = userIdBase
        userList.append(newUser)
        print(newUser)
        response = {
            'data': {},
            'meta': {
                'msg': 'new user added',
                'status': 201
            }
        }
        return json.dumps(response)
    testData = {
        'data': {
            'pagenum': 1,
            'total': 10,
            'users': userList
        },
        'meta': {
            'msg': '获取管理员列表成功',
            'status': 200
        }
    }
    return json.dumps(testData)


@app.route('/api/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUserInfoById(uid):
    print(request.method)
    if request.method == "PUT":
        userData = request.get_data().decode('utf-8')
        userData = json.loads(userData)
        for user in userList:
            if uid == user['id']:
                try:
                    print(userData)
                    user['email'] = userData.get('email')
                    user['mobile'] = userData.get('mobile')
                    res = {
                        'data': user,
                        'meta': {
                            'msg': '修改成功',
                            'status': 200
                        }
                    }
                    return json.dumps(res)
                except Exception:
                    return json.dumps({'data': {},
                                       'meta': {
                        'msg': '用户信息修改失败',
                        'status': 400
                    }})
    elif request.method == "GET":
        for user in userList:
            if uid == user['id']:
                res = {
                    'data': user,
                    'meta': {
                        'msg': '查询成功',
                        'status': 200
                    }
                }
                return json.dumps(res)
    elif request.method == "DELETE":
        for user in userList:
            if uid == user['id']:
                userList.remove(user)
                res = {
                    'data': None,
                    'meta': {
                        'msg': f'删除{uid}成功',
                        'status': 200
                    }
                }
                return json.dumps(res)
    return json.dumps({'data': None,
                       'meta': {
                           'msg': 'fail',
                           'status': 400
                       }})


@app.route('/api/users/<uid>/state/<stateType>', methods=['PUT'])
def changeUserState(uid, stateType):
    print(uid, stateType)
    for user in userList:
        if str(user.get('id')) == uid:
            user['mg_state'] = False if stateType == 'false' else True
            print(user)
            return json.dumps({
                'data': user,
                'meta': {
                    'msg': 'change user state success',
                    'status': 200
                }
            })
    return json.dumps({'data': '',
                       'meta': {
                           'msg': 'fail',
                           'status': 400
                       }
                       })


@app.route('/api/rights/<string:viewType>', methods=['GET'])
def getRightsList(viewType):
    print(viewType)
    if viewType == 'list':
        res = {
            'data': rightsList,
            'meta': {
                'msg': '获取权限列表成功',
                'status': 200
            }
        }
        return json.dumps(res)
    elif viewType == 'tree':
        res = {
            'data': rightsTree,
            'meta': {
                'msg': '获取权限列表成功',
                'status': 200
            }
        }
        return json.dumps(res)
    else:
        return {
            'data': {},
            'meta': {
                'msg': 'param not allowed',
                'status': 400
            }
        }


@app.route('/api/roles', methods=['GET'])
def getRolesList():
    if request.method == "GET":
        res = {
            'data': rolesList,
            'meta': {
                'msg': '获取角色列表成功',
                'status': 200
            }
        }
        return json.dumps(res)
    else:
        res = {
            'data': {},
            'meta': {
                'msg': 'method not allowed',
                'status': 400
            }
        }
        return json.dumps(res)


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(host='0.0.0.0', port=8000)
