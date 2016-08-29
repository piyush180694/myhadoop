#!/usr/bin/python2

import os
import sys
import base64

countpass = 3
while countpass != 0:
    #name = raw_input("Enter Name: ")
    passwd = raw_input("Enter Admin Password: ")
    passwd = base64.b64encode(passwd)
    if passwd == "YWRtaW4=":
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
datacount = 0
taskcount = 0

DATA = {}

IP = ""
Port = ""

namenodefile = open("/root/Desktop/namenodefile.txt","a+")
jobtrackerfile = open("/root/Desktop/jobtrackerfile.txt","a+")

while True:
    print           ('''
######################----CLUSTER SETTINGS----##########################

    ***************************************************************
    *                      (IMPORATANT)                           *
    *     (PLEASE CREATE THE CLUSTER BEFORE MOVING TO CLIENT)     *
    *                                                             *
    ***************************************************************
                    
                    I:-------NAMENODE-------
                      1.  Create Namenode
                      2.  Stop NameNode

                    II:------DATANODE-------
                      3.  Create DataNode
                      4.  Stop DataNode

                    III:----View HDFS Data----
                      5. Open Firefox for Data

                    IV:------JOBTRACKER-------
                      6.  Create JobTracker
                      7.  Stop JobTracker

                    V:-----TASKTRACKER------
                      8.  Create TaskTracker
                      9.  Stop TaskTracker

                    VI:-View MapReduce Data-
                      10. Open Firefox for Data

                    VII:--------EXIT--------
                      11. EXIT THIS WINDOW''')
    inp = raw_input("Enter your choice:")

    if inp == '1':
        f = open("/root/Desktop/free_disk.txt","r")
        
      
        

        for i in f.readlines():
                i = i.strip()
                print i
                IP = i
                port ="9001"
                print "Enter Directory Name: "
                IPS = IP +":"+ Port
	        os.system("sshpass -p redhat ssh -o StrictHostKeyChecking=no root@"+IP+" exit")
	        os.system("sshpass -p redhat scp /root/Desktop/name_auto.py root@"+IP+":/root/Desktop/name.py")	
                os.system("sshpass -p redhat ssh -X root@"+IP+" python /root/Desktop/name.py "+IPS+" "+inp)
              
    elif inp == '2':
        IP="192.168.0.1"
        port="9001"
        IPS=IP +":"+ port
        os.system("sshpass -p redhat ssh -X root@"+IP+" -o StrictHostKeyChecking=no python /root/Desktop/name_auto.py "+IPS+" "+inp)
	namenodefile.seek(0)

    elif inp == '3':
        f = open("/root/Desktop/free_disk.txt","r")

        count = raw_input("Enter number of DataNodes required: ")
        count = int(count)

        for i in f.readlines():
                i = i.strip()
                print i
                count -= 1
                IPdata = i
                 
                os.system("sshpass -p redhat ssh -o StrictHostKeyChecking=no root@"+IPdata+" exit")
                os.system("sshpass -p redhat scp /root/Desktop/data_auto.py root@"+IPdata+":/root/Desktop/data.py ")
                IPS = "192.168.0.1:9001"
                os.system("sshpass -p redhat ssh -X root@"+IPdata+" python /root/Desktop/data.py "+IPS+" "+inp)
                if count == 0:
                    break
        f.close()
     

    elif inp == '4':
	IPdata = raw_input("Enter The IPaddress of DataNode to STOP: ")
        os.system("sshpass -p 'redhat' ssh -X root@"+IPdata+" -o StrictHostKeyChecking=no python /root/Desktop/data.py "+IPdata+" "+inp)

    elif inp == '5':
        os.system("firefox 192.168.0.1:50070")
	namenodefile.seek(0)

    elif inp == '6':
        IP = raw_input("Enter The IPaddress for JobTracker:")
        Port = raw_input("Enter The PortNumber for JobTracker:")
        IPS = IP +":"+ Port
        IPS1="192.168.0.1:9001"
        os.system("sshpass -p redhat ssh -o StrictHostKeyChecking=no root@"+IP+" exit")
	os.system("sshpass -p redhat scp /root/Desktop/job_auto.py root@"+IP+":/root/Desktop/job.py  ")
        os.system("sshpass -p redhat ssh -X root@"+IP+"  python /root/Desktop/job.py "+IPS1+" "+IPS+" "+inp)
        jobtrackerfile.write(IPS)
	jobtrackerfile.seek(0)

    elif inp == '7':
        IP="192.168.0.1"
        IPS1="192.168.0.1:9001"
        IPS="192.168.0.1:9002" 
        os.system("sshpass -p 'redhat' ssh -X root@"+IP+" -o StrictHostKeyChecking=no python /root/Desktop/job.py "+IPS1+" "+IPS+" "+inp)
	jobtrackerfile.seek(0)

    elif inp == '8':
        f = open("/root/Desktop/free_ram.txt","r")

        count = raw_input("Enter number of TaskTrackers required: ")
        count = int(count)

        for i in f.readlines():
                i = i.strip()
                print i
                count -= 1
                IP = i
                IPS1="192.168.0.1:9001"
                IPS = "192.168.0.1:9002"
                os.system("sshpass -p redhat ssh -o StrictHostKeyChecking=no root@"+IP+" exit")
                os.system("sshpass -p redhat scp /root/Desktop/task_auto.py root@"+IP+":/root/Desktop/task.py ")
                os.system("sshpass -p redhat ssh -X root@"+IP+" python /root/Desktop/task.py "+IPS1+" "+IPS+" "+inp)
                if count == 0:
                    break

        f.close()


    elif inp == '9':
        #for i in f.readlines():
         #       i = i.strip()
          #      print i
        f = open("/root/Desktop/free_ram.txt","r")
        os.system("hadoop job -list-active-trackers")
        count = raw_input("Enter Number Of TaskTrackers WantTo Delete: ")
        count = int(count)

        for i in f.readlines():
                i = i.strip()
                print i
                count -= 1
                IP = i
               
                IPS1="192.168.0.1:9001"
                IPS = "192.168.0.1:9002"
                os.system("sshpass -p 'redhat' ssh -X root@"+IP+" -o StrictHostKeyChecking=no python /root/Desktop/task.py "+IPS1+" "+IPS+" "+inp)
                if count == 0:
                    break
        f.close()

    elif inp == '10':
        os.system("firefox 192.168.0.1:50030")
	jobtrackerfile.seek(0)
 
    else:
        break
    
    os.system("clear")
    nameport = namenodefile.read().split(":")
    jobport = jobtrackerfile.read().split(":")
	
namenodefile.close()
jobtrackerfile.close()

exit()

                  

                    
                
