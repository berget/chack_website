#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-28 12:23:05
# @Author  : berget (darkrewrite@gmail.com)
# @Link    : http://example.org
# @Version : $Id$
# 此模組是用來仿造 linux 的curl功能，避免同時存取

import os, sys
from datetime import datetime
import time
import re


class urlcrontab(object):
	"""
	    docstring for urlcrontab
	    建立一個排程執行緒，初始化需要傳入log路徑、url、pidfilename
	"""
	def __init__(self, logpath, url, pidfilename):
		self.logpath = logpath
		self.url = url
		self.pidfilename = pidfilename
	def urlcron_procedure(self):
		pidfilename = self.pidfilename
		#檢查pidfilename是否存在
		checkfile = Checkpid(pidfilename)
		pidfile = checkfile.runin_pid()
		if pidfile == True:
			print "%s already exists, exiting" % pidfilename
		else:
			pid = checkfile.getpid()
			# 寫入目前的pid
			file(pidfile, 'w').write(pid)
			try:
				print('run in:')
				starttime = time.time()
				st = datetime.fromtimestamp(starttime).strftime('%Y-%m-%d %H:%M:%S')
				print('start time:')
				print(st)
				url = self.url

				#call urltoolslib class
				curl = urltoolslib(url)
				response = curl.touchurl()
				endtime = time.time()
				et = datetime.fromtimestamp(endtime).strftime('%Y-%m-%d %H:%M:%S')
				overtime = endtime - starttime
				# 紀錄開始與結束時間，跟所費時間以及內容
				writestr = st + ',' + response + ','+ et + ',' + '花費時間：' + str(overtime) + '\n'
				logtime = datetime.fromtimestamp(starttime).strftime('%Y%m')
				logpath = self.logpath
				logfile = logpath +'/'+ pidfilename+'_'+logtime +'.log'
				wf = file(logfile, 'a+')
				wf.write(writestr)
				wf.close()
				print('OK')
			finally:
				# 移除檔案
				os.unlink(pidfile)

class Checkpid(object):
	"""
	    docstring for checkpid
	    傳入pidfilename，
	"""
	def __init__(self,pidfile_name=''):
		self.pid = str(os.getpid())
		if not pidfile_name:
			self.pidfile = "/tmp/"+"mydaemon.pid"
		else:
			self.pidfile = "/tmp/"+ pidfile_name + ".pid"
	#取得當前的pid
	def getpid(self):
		return self.pid

	def runin_pid(self):
		# 檢查目前是否正在執行中
		if os.path.isfile(self.pidfile):
			return True
		else:
			return self.pidfile



class urltoolslib(object):
	"""docstring for touchurl"""
	def __init__(self, url):
		self._request_headers = {
			"Accept-Language": "en-US,en;q=0.5",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0 ms/1.0",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Connection": "keep-alive" 
		}
		_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
		#沒有值，就不處理直接中斷程序
		assert _url, 'not url'
		self.url = _url[0]

	def touchurl(self):
		"""
		    使用urllib2的模組，進行網頁內容的讀取，並且判斷回傳狀態
		"""
		import urllib2

		try:
			request = urllib2.Request(self.url, headers=self._request_headers)
			response = urllib2.urlopen(request)
			status_code = response.code
			if status_code == 200:
				return response.read()

		except urllib2.HTTPError, e:
			status_code = e.code
			if status_code == 404:
				return "page not found"
			elif status_code == 403:
				return "Insufficient permissions"
			elif status_code == 500:
				return "Server Error"