from flask import Flask, request
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'
    if not allowed_file(file.filename):
        return 'File type not allowed'

    # 保存上传的图片
    img = Image.open(file)
    img.save('uploaded_image.jpg')

    # 使用pytesseract识别图片中的文字
    text = pytesseract.image_to_string(img, lang='eng')

    return text

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    from gevent import pywsgi

    server = pywsgi.WSGIServer(('192.168.0.106', 823), app)
    server.serve_forever()




# # 添加tesseract的路径
# pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
# """
# image_to_string()：如果识别英文或数字可以不必额外参数，如果识别其他语言则需要加上lang参数
# lang='chi_sim'表示要识别的是中文简体
# 没有识别出来时，返回空白
# """
# text = pytesseract.image_to_string(Image.open('test.png'), lang='chi_sim')
# print(text)
