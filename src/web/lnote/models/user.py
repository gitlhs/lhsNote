#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from config import db_config

'''
用户类
'''
class User(object):

    # 构造函数
    def __init__(self):
        
        self.db = pymysql.connect(**db_config.CONF)
        self.cur = self.db.cursor()

    # 通过邮箱获取用户信息
    def get_user_by_email(self, email):
        
        sql = "select * from user where email='%s'" % email
        self.cur.execute(sql)
        return self.cur.fetchone()

    # 析构函数
    # def __del__(self):
    #     self.db = None
    #     self.cur = None