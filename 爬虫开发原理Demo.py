import re
import requests
from bs4 import BeautifulSoup
import os
import urllib
# url = 'https://fanyi.baidu.com/translate'
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
# }
Img = re.compile( r'<img.*?data-original=[\'"](.*?\.(png|jpe?g|gif))[\'"].*?>')
def get_image(url, header):

    res = requests.get(url, headers=header)
    req = BeautifulSoup(res.text, "html.parser")
    ret = req.find_all('img')
    # 本地存储路径
    folder_path = './images/'

    # 如果存储路径不存在，则创建它
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    data = []
    for item in ret:  # soup.find_all对网页中的img—src进行迭代
        print(item)
        item = str(item)  # 转换为str类型
        Picture = re.findall(Img, item)  # 结合re正则表达式和BeautifulSoup, 仅返回超链接

        for b in Picture:  # 遍历列表，取最后一次结果
            data.append(b)
        # i = i + 1
            data.append(data[-1])
    print(data)
    ms = r'^http.*\.(png|jpg?g|gif)$'
    datas = re.findall(ms, data)
    print(datas)
    for image_url in datas:
        filename = os.path.join(folder_path, image_url.split('/')[-1])
        try:
            urllib.request.urlretrieve(image_url, filename)
        except urllib.error.URLError:
            print("下载不了")



get_image(
    "https://jiajuwang.huangye88.com/",
    header= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Cookie":"__bid_n=187b7217905b843ee64207; Hm_lvt_c8184fd80a083199b0e82cc431ab6740=1682404637; FPTOKEN=GB1+PkGjQfzULoIPSi5Zp9WJ2Rbp/qPSBsC62xB5mMPq26MgP2tJbIWzM/eimMIL/5Gy/XThcqPPmezd2uU2MSjKOWHhwa8hiMil/5rNKC3/IOnUUBMMHMOTLNZ9n10jE64Bm7aI8GpXlIwUcXF6+tqz0YOTxUYPb/5HiDiGHdIMjXwMt0ihGS65KSLidwzSOxSK2EKpEG1Re0OqLmKFG3koBFcYCCeDRnQaBSsVPXRrEywMoJzxhXoN/96f9Twt8SlD/ZoLV/mDtkXR0HY1x9k35b+mJTUpHy7Bz/FN46YPWRuq8Wf2RA24R5cjq0tAcfts5uFW5HPz47qmkI8GRtt9OWf0ImnBK0FYKso4GPFyb+85eX4Hp/PmCz9wlud+xbL0DSISJlGGoAjOzqLMOA==|o3TKVijXcA240qrum8AvyggVCuiAGh3gDcXj8HziZ1A=|10|585426640b8632ab6e78811be93ae8d3; PHPSESSID=16824046366821-80be3e4231d31d31434f9736d67c3cfa43c2f57d; Hm_lpvt_c8184fd80a083199b0e82cc431ab6740=1682404690"
}

)
