# x：需要绘制直方图的数据，可以是一个数组或序列。
# bins：指定直方图的条形数，或者指定每个条形的边界值。默认值为10。
# range：指定直方图的范围，即x轴的取值范围。默认值为None，表示使用数据的最大值和最小值作为范围。
# density：指定是否将直方图归一化。默认值为None，表示不进行归一化。
# cumulative：指定是否绘制累计直方图。默认值为False。
# histtype：指定直方图的类型，可以是’bar’、‘barstacked’、‘step’、‘stepfilled’。默认值为’bar’。
# align：指定直方图条形的对齐方式。默认值为’mid’，表示条形的中心与x轴上的标签对齐。
# orientation：指定直方图的方向，可以是’horizontal’或’vertical’。默认值为’vertical’。
# color：指定直方图的颜色。
# label：指定直方图的标签。
# alpha：指定直方图的透明度。
# edgecolor：指定直方图条形边缘的颜色。
# linewidth：指定直方图条形边缘的宽度。
# xticks、yticks：指定x轴、y轴上的刻度值。


import re
import requests
from bs4 import BeautifulSoup
import os
import urllib
url = 'https://jiajuwang.huangye88.com/'
header= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Cookie":"__bid_n=187b7217905b843ee64207; Hm_lvt_c8184fd80a083199b0e82cc431ab6740=1682404637; FPTOKEN=GB1+PkGjQfzULoIPSi5Zp9WJ2Rbp/qPSBsC62xB5mMPq26MgP2tJbIWzM/eimMIL/5Gy/XThcqPPmezd2uU2MSjKOWHhwa8hiMil/5rNKC3/IOnUUBMMHMOTLNZ9n10jE64Bm7aI8GpXlIwUcXF6+tqz0YOTxUYPb/5HiDiGHdIMjXwMt0ihGS65KSLidwzSOxSK2EKpEG1Re0OqLmKFG3koBFcYCCeDRnQaBSsVPXRrEywMoJzxhXoN/96f9Twt8SlD/ZoLV/mDtkXR0HY1x9k35b+mJTUpHy7Bz/FN46YPWRuq8Wf2RA24R5cjq0tAcfts5uFW5HPz47qmkI8GRtt9OWf0ImnBK0FYKso4GPFyb+85eX4Hp/PmCz9wlud+xbL0DSISJlGGoAjOzqLMOA==|o3TKVijXcA240qrum8AvyggVCuiAGh3gDcXj8HziZ1A=|10|585426640b8632ab6e78811be93ae8d3; PHPSESSID=16824046366821-80be3e4231d31d31434f9736d67c3cfa43c2f57d; Hm_lpvt_c8184fd80a083199b0e82cc431ab6740=1682404690"
}
Img = re.compile( r'<img.*?data-original=[\'"](.*?\.(png|jpe?g|gif))[\'"].*?>')


res = requests.get(url, headers=header)
req = BeautifulSoup(res.text, "html.parser")
ret = req.find_all('img', {"data-original": True})
# print(ret)
# # 本地存储路径
# folder_path = './images/'
# # 如果存储路径不存在，则创建它
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)
data = []
for item in ret:  # soup.find_all对网页中的img—src进行迭代
    item = str(item)  # 转换为str类型

    picture = re.findall(Img, item)
    for b in picture:  # 遍历列表，取最后一次结果
        data.append(b)
        b = str(b)
        # data.append(data[-1])
#

#     Picture = re.findall(Img, item)  # 结合re正则表达式和BeautifulSoup, 仅返回超链接
#     for b in Picture:  # 遍历列表，取最后一次结果
#         data.append(b)
#
#         data.append(data[-1])
#
# pattern = re.compile(r'^https?://.*\.(png|jpe?g|gif)$')
# listdata= []
# for x in data:
#     http_elements = [elem for elem in x if 'http' in elem]
#     if http_elements:
#         # 如果有包含http子字符串的元素，则展示这些元素
#         for elem in http_elements:
#             listdata.append(elem)
#     else:
#         # 如果没有包含http子字符串的元素，则删除整个元组
#         del x
# datelist=  []
# for item in listdata:
#
#     print(item[item.rindex("http"): item.rindex("_90Q")])
#     datelist.append(item[item.rindex("http"): item.rindex("@")])
#
# for e in datelist:
#     print()
#     filename = os.path.join(folder_path, e)
#     try:
#         urllib.request.urlretrieve(e, filename)
#     except urllib.error.URLError:
#         print("下载不了")
#



