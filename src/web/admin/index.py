#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import admin

@admin.route('/')
def index():
	return 'admin'