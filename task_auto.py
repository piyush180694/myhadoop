#!/usr/bin/python2

import os
import sys

IPS1 = sys.argv[1]
IPS = sys.argv[2]
inp = sys.argv[3]


if inp == '19':
		
		os.system("cd /etc/hadoop")
		core = IPS1
                job = IPS
		c = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://"""+core+"""</value>
</property>
</configuration>"""

		m = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>"""+job+"""</value>
</property>
</configuration>"""
		
		f = open("/etc/hadoop/core-site.xml","w+")
		f.write(c)
		f.close()
		f = open("/etc/hadoop/mapred-site.xml","w+")
		f.write(m)
		f.close()	
		os.system("/usr/java/jdk1.7.0_51/bin/jps")
		print
		os.system("hadoop-daemon.sh start tasktracker")
		os.system("/usr/java/jdk1.7.0_51/bin/jps")
elif inp == '20':
		os.system("hadoop-daemon.sh stop tasktracker")
else:
		exit()
	
