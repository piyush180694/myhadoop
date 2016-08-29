#!/usr/bin/python2

import os
import sys
import base64

os.system('clear')
countpass = 3
while countpass != 0:
    passwd = raw_input("Enter Client Password: ")
    passwd = base64.b64encode(passwd)
    if passwd == "Y2xpZW50":
        print "Password ACCEPTED\n\nWELCOME "
        break
    else:
        print "SORRY WRONG PASSWORD...TRY AGAIN"
        countpass -= 1
        print str(countpass)+" tries left"
        continue
else:
    print "YOU HAVE EXCEEDED YOUR TRIES...PLEASE TRY AGAIN LATER"
    exit()

#nameip = raw_input("Enter NameNode IP: ")
#jobip = raw_input("Enter JobTracker IP: ")
#port = raw_input("Enter PortNumber: ")

namenodefile = open("/root/Desktop/namenodefile.txt","r")
jobtrackerfile = open("/root/Desktop/jobtrackerfile.txt","r")
port='1111'

while True:
    os.system("clear")
    print           ('''
###########################----MENU----##########################
                    I:--------:MAIN:--------
                      1. Setup
		      2. Write Data
		      3. Remove Data
		      4. View Data Cluster
                      5. Run Job
                      6. EXIT PROGRAM''')

    inp = raw_input("Enter your choice:")

    if inp == '1':
        print 
        rep = raw_input("Enter Replications Required:")
        print 
        block = raw_input("Enter Block Size in MB:")
        block = int(block) * 1024 * 1024
	block = str(block)
        s =  """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.replication</name>
<value>"""+rep+"""</value>
</property>
<property>
<name>dfs.block.size</name>
<value>"""+block+"""</value>
</property>
</configuration>"""
    
        c ="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://"""+nameip+":"+port+"""</value>
</property>
</configuration>"""
        m = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>mapred.job.tracker</name>
<value>"""+jobip+"""</value>
</property>
</configuration>"""
        
        f = open("/etc/hadoop/hdfs-site.xml","w+")
	f.write(s)
	f.close()
        f = open("/etc/hadoop/core-site.xml","w+")
	f.write(c)
	f.close()
        f = open("/etc/hadoop/mapred-site.xml","w+")
	f.write(m)
	f.close()
	
    elif inp == '2':
	filename = raw_input("Enter Filename: ")
	os.system("hadoop fs -put "+filename+" /")

    elif inp == '3':
	os.system("hadoop fs -ls /")
	filename = raw_input("Enter Filename to remove: ")
	os.system("hadoop dfs -rmr hdfs:///"+filename)
	
    elif inp == '4':
	os.system("hadoop fs -ls /")
	raw_input()

    elif inp == '5':
	filename = raw_input("Enter FileName to Run Job on: ")
	mapper = raw_input("Provide mapper program: ")
 	reducer = raw_input("Provide reducer program: ")
	out = raw_input("Enter Output FileName: ")
	while True:
            os.system("clear")
            print           ('''
###########################----MENU----##########################
                    I:--------:MAIN:--------
                      1. ReadyMade
                      2. Program File''')
            enter = raw_input("Enter your choice:")

            if enter == '1':
                filename = raw_input("Enter FileName to Run Job on: ")
                mapper = raw_input("Mapper code: ")
                reducer = raw_input("Reducer code: ")
                out = raw_input("Enter Output FileName: ")
                os.system("hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -input /"+filename+" -mapper "+mapper+" -reducer "+reducer+" -output /"+out)
            else:
                filename = raw_input("Enter FileName to Run Job on: ")
                mapper = raw_input("Mapper code: ")
                mapp = open("/root/Desktop/"+mapper,"r")
                reducer = raw_input("Reducer code: ")
                reduc = open("/root/Desktop/"+reducer,"r")
                out = raw_input("Enter Output FileName: ")
                os.system("hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -input /"+filename+" -mapper ./"+mapper+" -file -reducer ./"+reducer+" -file -output /"+out)
    
    else:
		exit()


