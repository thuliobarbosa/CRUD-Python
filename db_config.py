#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:31:05 2021

@author: ely
"""

from server import app
from flaskext.mysql import MySQL
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = '2EyRmeqEIM'
app.config['MYSQL_DATABASE_PASSWORD'] = 'BX0FuGP29S'
app.config['MYSQL_DATABASE_DB'] = '2EyRmeqEIM'
app.config['MYSQL_DATABASE_HOST'] = 'remotemysql.com'
mysql.init_app(app)
