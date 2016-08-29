#!/usr/bin/python2

import os
import sys

g = open("/root/Desktop/RAM2.txt","r")

for i in  g.readlines():
    i = i.strip()
    count2 += 1

print count2

g.close()
