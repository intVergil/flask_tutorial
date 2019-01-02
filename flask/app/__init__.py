from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#创建app应用,__name__是python预定义变量，被设置为使用本模块.
app = Flask(__name__)

#添加配置信息
app.config.from_object(Config)
#建立数据库关系
db = SQLAlchemy(app)
#绑定app和数据库，以便进行操作
migrate = Migrate(app,db)

from app import routes,models