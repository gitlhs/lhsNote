#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from config import db_config

'''
笔记类
'''
class Note(object):

    # 构造函数
    def __init__(self):
        pass
        # self.db = pymysql.connect(**db_config.db_conf['%s'])
        # self.cur = self.db.cursor()

    # 获取某个用户的所有笔记
    def get_notes(self, userid):
        pass

    # 析构函数
    # def __del__(self):
    #     self.db = None
    #     self.cur = None