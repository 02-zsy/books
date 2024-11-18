# 数据库连接配置
SQL_USERNAME = "root"
SQL_PASSWORD = "root"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "books"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(
    SQL_USERNAME, SQL_PASSWORD, HOST, PORT, DATABASE)


# 返回正常汉字格式
JSON_AS_ASCII = False