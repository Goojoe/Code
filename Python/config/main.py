import configparser as cp

config_path = "./config.ini"

# 实例化对象
config = cp.ConfigParser()
# 读取配置文件
config.read(config_path, "utf-8")
# 赋值
db = config['db']['ip']

print(db)
# print(config.get("db","ip"))