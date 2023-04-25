#coding=UTF-8
from db import DB
from flask import Flask, jsonify, Response

import json
app = Flask(__name__)
db = DB('localhost', 'root', '123456', 'test')
results = db.execute_query('SELECT * FROM test')
# Python 对象（通常是字典或列表）序列化为一个 JSON 字符串。[{"id": 1, "name": "张三", "age": 2}, {"id": 2, "name": "里斯", "age": 23}, {"id": 3, "name": "王5", "age": 234}]
json_str = json.dumps(results, ensure_ascii=False)
@app.route('/dataList',methods=['get'])
def get_data():
    json_str = json.dumps(results, ensure_ascii=False)
    return Response(json_str, content_type="application/json; charset=utf-8")
if __name__ == '__main__':
    app.run(debug=True, port=8888, host='0.0.0.0')
db.close_conn()