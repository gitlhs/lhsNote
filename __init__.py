from flask import Flask
#导入accout 和order
from fcrm.views import accout
from fcrm.views import order
app = Flask(__name__)
print(app.root_path)  #根目录

app.register_blueprint(accout.accout)  #把蓝图注册到app里面，accout.accout是创建的蓝图对象
app.register_blueprint(order.order)