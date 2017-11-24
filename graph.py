#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rrdtool
import time
def createpng(hostname):
	datapatch = "/root/rrddata/"
	pngpatch = "/root/rrdpng/"
	fname = datapatch + hostname + ".rrd"
	dname = pngpatch + hostname +"_daily"+ ".png"
	wname = pngpatch + hostname +"_weekly"+ ".png"
	mname = pngpatch + hostname +"_monthly"+ ".png"
	yname = pngpatch + hostname +"_yearly"+ ".png"
	dtitlename = "Daily net IO rate graph"
	wtitlename = "Weekly net IO rate graph"	
	mtitlename = "Monthly net IO rate graph"
	ytitlename = "Yearly net IO rate graph"
	rrdtool.graph(dname,"--title="+dtitlename,"--vertical-label=Bytes per second",\
                "--x-grid","MINUTE:12:HOUR:1:HOUR:1:0:%H","--color=CANVAS#FFFFFF",\
                "--width","600","--height","300",
                "DEF:inoctets="+fname+":netup:AVERAGE",
                "DEF:outoctets="+fname+":netdown:AVERAGE",
                #"CDEF:total=inoctets,outoctets,+",
                #"LINE1:total#FF8833: Total traffic",
                "AREA:inoctets#00FF00:In traffic",
                "LINE1:outoctets#0000FF: Out traffic",
                "COMMENT:\\r",
                "COMMENT:\\r",
                "GPRINT:inoctets:AVERAGE:AVG In traffic\:%21lf Bytes",
                "COMMENT: ",
                "GPRINT:inoctets:MAX:MAX In traffic\:%21lf Bytes",
                "COMMENT: ",
                "GPRINT:outoctets:AVERAGE:AVG Out traffic\:%21lf Bytes",
                "COMMENT: ",
                "GPRINT:outoctets:MAX:MAX Out traffic\:%21lf Bytes")

	rrdtool.graph(wname,"--title="+wtitlename,"--vertical-label=Bytes per second","--start=end-1w","--end=00:00",\
                "--color=CANVAS#FFFFFF",\
                "--width","600","--height","300",
                "DEF:inoctets="+fname+":netup:AVERAGE",
                "DEF:outoctets="+fname+":netdown:AVERAGE",
                "CDEF:total=inoctets,outoctets,+",
                "LINE1:total#FF8833: Total traffic",
                "AREA:inoctets#00FF00:In traffic",
                "LINE1:outoctets#0000FF: Out traffic",
                "COMMENT:\\r",
                "COMMENT:\\r",
                "GPRINT:inoctets:AVERAGE:AVG In traffic\:%21lf Bytes",
                "COMMENT: ",
                "GPRINT:inoctets:MAX:MAX In traffic\:%21lf Bytes",
                "COMMENT: ",
                "GPRINT:outoctets:AVERAGE:AVG Out traffic\:%21lf Bytes",
                "COMMENT: ",
                "GPRINT:outoctets:MAX:MAX Out traffic\:%21lf Bytes")

