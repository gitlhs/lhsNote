#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

lnote = Blueprint(
	'lnote',
	__name__,
	template_folder = 'templates',   # 模板所在文件夹的名字
	static_folder   = 'static',      # 静态文件所在文件的名字
	static_url_path = '/s' 			# 静态文件访问url路径
)

from . import index