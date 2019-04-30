#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import lnote
from flask import render_template,request,redirect,url_for,session
from models.user import User
from libraries import utils

'''
首页
'''
@lnote.route('/')
def index():
	# 未登录，则跳转到登录页面
	if not utils.has_login():
		return redirect(url_for('.login'))
	# 已登录状态，则传递用户数据并展示首页
	data = {
		'userid'  : session['userid'],
		'nickname': session['nickname']
	}
	return render_template('index.html',data=data)

'''
 退出登录接口
'''
@lnote.route('/logout_cgi',methods = ['POST','GET'])
def logout_cgi():
	session['userid'] = ''
	return utils.cgi_json(0, '退出登录成功')
	


'''
注册页面
'''
@lnote.route('/regist')
def regist():
	return render_template('regist.html')

'''
注册接口
'''
@lnote.route('/regist_cgi')
def regist_cgi():
	# 获取并检查页面传来的参数
	email = request.values.get('email')
	password = request.values.get('password')
	nickname = request.values.get('nickname')
	code = request.values.get('code')
	if not email:
		return utils.cgi_json(1, '邮箱不能为空')
	if not password:
		return utils.cgi_json(2, '密码不能为空')
	# 判断邮箱是否已被注册，验证：密码昵称验证码

'''
登录页面
'''
@lnote.route('/login')

def login():
	return render_template('login.html')

'''
登录接口
'''
@lnote.route('/login_cgi', methods=['POST'])
def login_cgi():
	
	# 获取并检查页面传来的参数
	email = request.values.get('email')
	password = request.values.get('password')
	if not email:
		return utils.cgi_json(1, '邮箱不能为空')
	if not password:
		return utils.cgi_json(2, '密码不能为空')

	# 通过邮箱获取用户信息
	user_obj = User()
	user_info = user_obj.get_user_by_email(email)
	if not user_info:
		return utils.cgi_json(3, '用户不存在')

	# 判断密码是否正确
	if password != user_info['password']:
		return utils.cgi_json(4, '密码不正确')

	# 生成登录态
	utils.set_login(user_info)

	# 返回登录成功
	return utils.cgi_json(0, '登录成功')

'''
判断用户是否登录
'''
def has_login():
	if 'userid' in session and session['userid']:
		return true
	return False







