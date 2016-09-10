#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-05 17:42:18
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sqlite3
import time


class sql_event(object):
	"""docstring for sql_enven"""
	def __init__(self, filepath):
		if not os.path.isfile(filepath):
			self.db_create(filepath)
			print 'db create OK'
                        import sys
                        sys.exit()
		else:
			self.conn = sqlite3.connect(filepath)

	def db_create(self, filepath):
		conn = sqlite3.connect(filepath)
		conn.execute('''CREATE TABLE COMPANY 
		               (ID INT PRIMARY KEY NOT NULL,
		                C_NID INT NOT NULL,
		                CNAME TEXT NOT NULL, 
		                URL TEXT NOT NULL,
		                UPDATA CHAR(50));''')
                conn.execute(''' CREATE TABLE JOBLIST
                                 (ID INT PRIMARY KEY NOT NULL,
                                  FOR104ID INT NOT NULL,
                                  C_NAME TEXT NOT NULL,
                                  FOR104URL TEXT NOT NULL
                                  UPDATA CHAR(50)); ''')
                conn.commit()
                print 'create tables'
        def db_getmaxID(self):
            conn = self,conn
            id_max = conn.execute('SELECT max(ID) FROM COMPANY')
            for id_data in id_max:
                if id_data[0] == None:
                    max_value = 1
                else:
                    max_value = id_data[0] + 1

	def db_INSERT_COMPANY(self, companyID, companyName, URL):
		insert_time = time.time()
       
		conn.execute('INSERT INTO COMPANY (ID, C_NID, CNAME, URL, UPDATA) VALUES(?, ?, ?, ?, ?)',[max_id_value, companyID, companyName, URL, insert_time])
		conn.commit()
		return True

        def db_INSERT_104JOB(self, jobID, titleName, 104Url):
            conn = self.conn
            conn.execute('INSERT INTO JOBLIST (ID, FOR104ID, C_NAME, FOR104URL, UPDATA VALUES(?, ?, ?, ?, ?)', [max_id_value, jobID, titleName, 104Url])

        

if __name__ == '__main__':
	sqlobj = sql_event('test.db')
	sqlobj.db_INSERT(companyID, companyName, URL)
