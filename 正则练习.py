import re
# str="https://csdnnews.blog.csdn.net/article/details/130333678?spm=1000.2115.3001.5927"
# ms = r'\d+'
# res = re.findall(ms, str)
# print(res)
# res1 = str[str.rindex("2115"): str.rindex(".300")]
# print(res1)
# 在上述代码中，正则表达式的含义解释如下：
#
# ^ 表示匹配字符串的开头。
# (?=.*[a-z]) 表示必须包含至少一个小写字母。
# (?=.*[A-Z]) 表示必须包含至少一个大写字母。
# (?=.*\d) 表示必须包含至少一个数字。
# (?=.*[-+&*@]) 表示必须包含至少一个特殊字符 +-&*@。
# [A-Za-z\d-+&*@]+ 表示匹配至少一个大小写字母、数字或特殊字符 +-&*@。
# $ 表示匹配字符串的结尾。
# 综上，以上代码可以校验输入的账号是否符合要求，并在不符合要求时提示用户重新输入。
def validate_account(account):
    pattern = r'^(?=.*[a-z])[A-Za-z\d-+&*@]+$'
    # 使用正则表达式匹配字符串，判断其是否符合要求
    if re.match(pattern, account):
        return True # 匹配成功，返回True
    else:
        return False # 匹配失败，返回False


while True:
    account = input("请输入账号：")
    if validate_account(account): # 调用validate_account()函数校验账号
        print("输入正确，账号为：", account)
        break
    else:
        print("账号格式不正确，请重新输入！")