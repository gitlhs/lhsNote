#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import lnote
from flask import render_template

@lnote.route('/')
def index():
	return render_template('index.html')