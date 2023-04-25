
# 登录接口
from db import DB
from flask import Flask, jsonify, Response, request
from datetime import datetime, timedelta
from PIL import Image
import pytesseract
import json
import jwt
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'   # 设置应用程序密钥，用于JWT签名和验证
db = DB('localhost', 'root', '123456', 'test') #库名
results = db.execute_query('SELECT * FROM denglu') #表名
users = {}
for t in results:
    users[t['username']] = str(t['password'])

@app.route('/login', methods=['post'])
def login_get():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({"token": json.dumps(token), 'success': True, 'message': '登录成功', "code": 200}), 200
    else:
        return jsonify({'success': False, 'message': '用户名或密码错误', "code": 1000})
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization', None)
    if not token:
        return jsonify({"error": "Missing token"}), 401
    try:
        data = jwt.encode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    except jwt.DecodeError:
        return jsonify({"error": "Invalid token"}), 401
    return jsonify({"message": "Hello, {}!".format(data['username'])}), 200

@app.route('/register',methods=['post'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
        return jsonify({'message': '缺少必要参数'}), 400

    for items in users:
        if items == username:
            return jsonify({'message': '该用户名已被注册'})
    insert_query = "INSERT INTO denglu (username, password) VALUES (%s, %s)"
    values = list(data.values())
    db.execute_insert(insert_query, values)
    db.close_conn()
    return jsonify({'message': '注册成功'})

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'
    file = request.files['file']
    print(file)
    # if file.filename == '':
    #     return 'No file selected'
    # if not allowed_file(file.filename):
    #     return 'File type not allowed'
    pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
    # 保存上传的图片
    img = Image.open(file)
    print(img)
    # img.convert('RGB')
    # img.save('uploaded_image.png')
    # print(img)
    # 使用pytesseract识别图片中的文字
    text = pytesseract.image_to_string(img, lang='chi_sim')

    return text
    print(text)
# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'jpg', 'png'}

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
if __name__ == '__main__':
    from gevent import pywsgi
    server = pywsgi.WSGIServer(('192.168.0.106', 8888), app)
    server.serve_forever()
db.close_conn()







