#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2
from urllib2 import URLError
from login import zabbix_login
import time

t = zabbix_login()


def graph_get(itemid1, itemid2):
    itemid = [itemid1, itemid2]
    netdata = []
    netclock = []
    for item in itemid:
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "history.get",
                "params": {
                    "output": "extend",
                    "history": 3,
                    "itemids": item,
                    "sortfield": "clock",
                    "sortorder": "DESC",
                    "limit": 1
                },
                "auth": t.user_login(),
                "id": 1,
            })
        request = urllib2.Request(t.url, data)
        for key in t.header:
            request.add_header(key, t.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()

            for graph in response['result']:
                clock = graph["clock"]
                clock = int(clock)
                time_local = time.localtime(clock)
                clock = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                netdata.append(graph["value"]),
                # print graph["clock"],
                netclock.append(graph["clock"])
    return netdata, netclock
