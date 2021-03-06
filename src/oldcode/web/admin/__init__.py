#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

admin = Blueprint(
	'admin',
	__name__,
	template_folder = 'templates',   # 模板所在文件夹的名字
	static_folder   = 'static',      # 静态文件所在文件的名字
)

from . import index