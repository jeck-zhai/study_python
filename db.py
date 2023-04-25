import mysql.connector

class DB:
    # 初始化类时需要传入数据库的连接信息，包括主机名（host）、用户名（username）、密码（password）和数据库名（database）
    def __init__(self, host, username, password, database):#库名
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        # 创建与数据库的连接
        self.conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )

    # 执行查询操作并返回结果
    def execute_query(self, query):
        cursor = self.conn.cursor() #创建一个游标对象
        cursor.execute(query)  # 执行 sql语句
        result = cursor.fetchall() #获取数据库数据
        fields = [field[0] for field in cursor.description]  #获取字段名称
        res = [dict(zip(fields, result)) for result in result] #转化为 {key:value}

        return res

        # 执行插入操作并返回结果
    def execute_insert(self, insert_query, values):
        cursor = self.conn.cursor()  # 创建一个游标对象
        cursor.execute(insert_query, values)  # 执行 sql语句
        self.conn.commit()  # 提交事务

        return cursor.lastrowid
    # 关闭与数据库的连接
    def close_conn(self):
        self.conn.close()
