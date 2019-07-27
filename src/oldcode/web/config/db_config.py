#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
数据库配置文件

'''

import pymysql
from config import base_config


db = {}

# 开发环境
db['development'] = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "passwd":"2209",
    "db": "lnote",
    "charset": "utf8",
    "use_unicode": True,
    "autocommit" : True,
    "cursorclass": pymysql.cursors.DictCursor
}


# 测试环境
db['test'] = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "passwd":"",
    "db": "lnote",
    "charset": "utf8",
    "use_unicode": True,
    "autocommit" : True,
    "cursorclass": pymysql.cursors.DictCursor
}


# 线上环境
db['production'] = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "passwd":"",
    "db": "lnote",
    "charset": "utf8",
    "use_unicode": True,
    "autocommit" : True,
    "cursorclass": pymysql.cursors.DictCursor
}

'''
数据库配置全局变量
'''
CONF = db[base_config.ENVIRONMENT]




