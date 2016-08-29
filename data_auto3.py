#!/usr/bin/python2

import os
import sys

IP = sys.argv[1]
inp = sys.argv[2]

print IP,inp

if inp == '11':
		directory = 'projdata'
		os.system("mkdir /"+directory)
		os.system("cd /etc/hadoop")
		core = IP
		s = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/"""+directory+"""</value>
</property>
</configuration>"""

		c = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://"""+core+"""</value>
</property>
</configuration>"""


		f = open("/etc/hadoop/hdfs-site.xml","w+")
		f.write(s)
		f.close()
		f = open("/etc/hadoop/core-site.xml","w+")
		f.write(c)
		f.close()	
		os.system("/usr/java/jdk1.7.0_51/bin/jps")
		print
		os.system("hadoop-daemon.sh start datanode")
		os.system("/usr/java/jdk1.7.0_51/bin/jps")
elif inp == '12':
		os.system("hadoop-daemon.sh stop datanode")
else:
		exit()
	
