import string
# res = 'I aM xXx'
#
# # 大小写互转
# print(res.capitalize())  #首字母大写
# print(res.title())  #返回一个标题形式的字符串
# print(res.swapcase()) #字符串大小写互转
# print(res.lower()) # 所有的字符串转为小写
# print(res.upper()) #所有字符串转为大写
# print(res.casefold()) #所有字符串转为小写

# 字符串填充
res = 'whoareyou'
res1 = '123123'
print(res.center(20, '#'))
# print("test".center(10, "*"))
print(res.ljust(20, '#')) #返回一个原字符串左对齐   whoareyou###########
print(res.rjust(20, '#')) #返回一个原字符串右对齐   ###########whoareyou
print(res.zfill(20)) #返回一个原字符串右对齐 使用0代替  00000000000whoareyou


#字符串编码

#字符串查找
