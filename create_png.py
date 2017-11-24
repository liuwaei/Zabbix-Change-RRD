#!/ubr/bin/env python
# -*- coding: utf-8 -*-
import os
import rrdtool
import time
from login import zabbix_login
from get_host import hostid_get
from get_item import item_get
from get_data import graph_get
from create import createrrd
from graph import createpng

start = time.time()
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
t = zabbix_login()
hostid, hostname = hostid_get()
itemid = []
i = 0
#for i in range(len(hostid)):
for i in range(50):
	hosts=str(hostname[i])
	print hosts
	createpng(hosts)
end = time.time()
print end-start
print "========================================================="
print "\r"
