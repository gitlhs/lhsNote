#!/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Blueprint


'''
添加默认搜索路径
'''
import sys
import os
pp_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上上级目录，即网站根目录
sys.path.append(pp_path)  # 将网站根目录加入默认搜索路径，以便其他文件引用config目录下的配置文件


lnote = Blueprint(
    'lnote',
    __name__,
    template_folder = 'templates',   # 模板所在文件夹的名字
    static_folder   = 'static',      # 静态文件所在文件的名字
    static_url_path = '/s'           # 静态文件访问url路径
)

from . import index