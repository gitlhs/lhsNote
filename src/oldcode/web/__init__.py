#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 包含在web文件夹里

import sys
from flask import Flask
from .admin import admin
from .lnote import lnote
from config import base_config

'''
实例化flask对象
'''
app = Flask(
	__name__,
	template_folder = 'templates',   # 模板所在文件夹的名字
	static_folder   = 'static',      # 静态文件所在文件的名字
	instance_relative_config = True, # 允许设置配置文件目录
	instance_path = base_config.CONFIG_PATH    # 配置文件目录
)


'''
引入基础配置文件
'''
app.config.from_pyfile('base_config.py')


'''
把蓝图注册到app里面
'''
app.register_blueprint(admin, subdomain='admin')
app.register_blueprint(lnote)
