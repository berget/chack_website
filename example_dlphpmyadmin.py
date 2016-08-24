#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-23 15:03:25
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : 0.1
# 抓取phpmyadmin，可指定版本，直接於主機上下載


import os
import re
import usingUrllib


from bs4 import BeautifulSoup

url = "https://www.phpmyadmin.net/downloads/"
#set phpmyadmin varsion
dl_phpmyadmin_varsion = "4.4.15"
dl_str = 'all-languages.tar.gz'

#get html data
urllib = usingUrllib.urltoolslib(url);
webdata = urllib.touchurl();

soup = BeautifulSoup(webdata)
for a in soup.find_all('a', href=True):
	a_link = a['href']
	#check http url
	_url = re.findall('http[s]?://files.phpmyadmin.net/phpMyAdmin/'+ dl_phpmyadmin_varsion +'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', a_link)
	if _url and  dl_str in _url[0]:
		
		if re.match(r'(.*)all-languages.tar.gz$', _url[0] ) :
			url = _url[0]
			geturldata = usingUrllib.urltoolslib(url);
			urldata = geturldata.touchurl();
			#set dl filename
			filenamelist = url.split('/')
			print filenamelist[-1]
			filename = filenamelist[-1]
			#save file
			with open(filename, "wb") as code:
				code.write(urldata)


if os.path.isfile(filename) :
	#
	import tarfile
	t = tarfile.open(filename, 'r')
	t.extractall()
	
	dirname = filename.split('.tar.gz')
	os.rename(dirname[0], "/tmp/phpmyadmin")



			






			
