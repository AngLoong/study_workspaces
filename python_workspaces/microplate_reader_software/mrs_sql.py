"""
处理数据库相关的操作
"""

import sqlite3
import time


class SqlDatabase(object):

    def __init__(self):
        self.con = sqlite3.connect("./data/sql/database.db")
        self.cc = SqlDatabase.sql_con.cursor()

    def __str__(self):
        pass

    


