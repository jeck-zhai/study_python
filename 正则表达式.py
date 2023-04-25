import re

# r = r"\d+" #正则表达式表示匹配连续的多个数值(第一连续的)  112
# r = r'b\d+'  #表示匹配b后面的连续数字  b6711
# r = r'ab+'
# r = r'ab*'
#
# m = re.search(r, "YRY1ab1abR5b6711eruwg")
# print(m)

# 1, 匹配数字
# text = "my nacme is zhacngs, i'm 19 year old, i hacve 2000 money"
# m = '\d+'
# res = re.findall(m, text)  #返回string中所有与m匹配的全部字符串,返回形式为数组
# print(res)
# 2, 匹配字母
# s = '\w+'
# ress = re.findall(s, text)
# print(ress)
# 3, 匹配空格
# ms = '\s+'
# print(re.findall(ms, text))
# 4, 匹配特定字符
# text1 = "my nacme is zhacngs, i'm 19 year old, i hacve 2000 money"
# mss = "[cm]a"
# print(re.findall(mss, text1))
# 4, 匹配重复字符 *
# res = "banabaneesdf"
# resm = 'a*'
# print(re.findall(resm, res))
# 获取url中的数字  是用正则表达式
str = 'https://blog.csdn.net/m0_60720471/article/details/129527579'
ms = r'\d+'
res = re.findall(ms, str)
print(str[str.rindex('dn'): len(str)]);
str= ('https://oss10.huangye88.net/live/user/2899999/1671841446012865500-0.jpg@1e_1c_108w_68h_90Q" src="//static.huangye88.cn/images/none/xiaofeipin.jpg', 'jpg')
# str[start:end]
# str.rindex('/')  字符穿方法,rindex()查找字符串str中最后一个'/'的位置,并返回该位置的搜索




