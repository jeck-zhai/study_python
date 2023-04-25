# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



# import mysql.connector
#
# # 建立数据库连接
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",#用户名
#   password="123456", #密码
#   database="test" #自己设置的数据库的名称
# )
#
# # 执行 SQL 查询
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM test")  #text  自己设置的数据库额名称
#
# # 获取查询结果
# result = mycursor.fetchall()
# print(result)
# for row in result:
#   print(row)