#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
基础配置文件

本文件设置一些公共的基础配置项
'''


'''
当前环境

开发环境：development
测试环境：test
线上环境：production
'''
ENVIRONMENT = 'development'


'''
是否调试模式
'''
if ENVIRONMENT == 'production':
	DEBUG = False
else:
	DEBUG = True


'''
网站根目录
'''
BASE_PATH = '/Users/linxiaoming/github_mine/lhsNote2/src/web'


'''
配置文件目录
'''
CONFIG_PATH = BASE_PATH + '/config'


'''
网站域名
'''
if ENVIRONMENT == 'production':
	SERVER_NAME = 'lnote.xyz'
else:
	SERVER_NAME = '127.0.0.1:5000'


'''
session的加密key
'''
SECRET_KEY = 'lnot@2019#!$'