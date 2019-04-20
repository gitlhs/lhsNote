#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Flask,session


'''
生成接口要返回的json数据
'''
def cgi_json(ret = 0, msg = '', data = None):
    ret = { 'ret' : ret, 'msg' : msg}
    if data:
        ret['data'] = data
    return json.dumps(ret)

'''
生成登录态
'''
def set_login(user_info):
    session['userid']   = user_info['useid']
    session['nickname'] = user_info['nickname']
    session['email']    = user_info['email']
    return True

'''
判断当前用户是否已登录
'''
def has_login():
    if 'userid' in session and session['userid']:
        return True
    return False

