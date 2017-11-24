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
for i in range(100):
    print hostname[i]
    start=0
    itemid.append(item_get(hostid[i]))
    a, b = graph_get(itemid[i][4], itemid[i][7])
    fname = '/root/rrddata/' + hostname[i] + '.rrd'
    fname=str(fname)
    file = os.path.exists(fname)
    print hostname[i],file
    if file == False:
        rrd = rrdtool.create(fname,'--step', '300', '--start','N',
                         'DS:netup:GAUGE:600:0:U',
                         'DS:netdown:GAUGE:600:0:U',
                         'RRA:AVERAGE:0.5:1:288',
                         'RRA:AVERAGE:0.5:6:1440',
                         'RRA:AVERAGE:0.5:12:8640',
                         'RRA:MAX:0.5:1:2880')
    i = i + 1
end = time.time()
print end-start
print "========================================================="
print "\r"
