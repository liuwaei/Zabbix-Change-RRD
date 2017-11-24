#!/ubr/bin/env python
# -*- coding: utf-8 -*-
import os
import rrdtool
import time
import datetime
from login import zabbix_login
from get_host import hostid_get
from get_item import item_get
from get_data import graph_get
from create import createrrd
from graph import createpng

stime = datetime.datetime.now()
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
t = zabbix_login()
hostid, hostname = hostid_get()
itemid = []
i = 0
#for i in range(len(hostid)):
for i in range(100):
    start=0
    itemid.append(item_get(hostid[i]))
    a, b = graph_get(itemid[i][4], itemid[i][7])
    fname = '/root/rrddata/' + hostname[i] + '.rrd'
    fname=str(fname)
    if len(a)!=0:
    	netupdata = str(a[0])
    	netdowndata = str(a[1])
    	starttime = str(b[0])
	print netupdata,netdowndata,starttime
	try:
   		update=rrdtool.update(fname,'%s:%s:%s' % (str(starttime),str(netupdata),str(netdowndata)))
		print hostname[i],update
	except:
		print hostname[i]+" err"
    i = i + 1
etime = datetime.datetime.now()
print (etime - stime).seconds
print "========================================================="
print "\r"
