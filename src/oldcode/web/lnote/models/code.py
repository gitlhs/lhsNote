#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from config import db_config

'''
验证码类
'''
class Code(object):

    # 构造函数
    def __init__(self):
        
        self.db = pymysql.connect(**db_config.CONF)
        self.cur = self.db.cursor()

    # 插入一条验证码数据
    def insert_code(self):
        
        sql = "insert * from user where email='%s'" % email
        self.cur.execute(sql)
        return self.cur.fetchone()
    # 查询该验证码

        

    # 析构函数
    # def __del__(self):
    #     self.db = None
    #     self.cur = None