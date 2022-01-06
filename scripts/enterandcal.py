#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from mypkg.srv import color
import sys

rospy.init_node('sevice_client')
rospy.wait_for_sever('rullet_judge')

def shoukinn(a,b,c,d):
    if a==b:
        return c*d
    else
        return 0

rullet_ok=rospy.ServiceProxy('rullet_judge',color)
decide = input("0:2倍？ 1:4倍?")
salary= input("いくらかける?")
number=input("何番?")
if decide==0:
    rullet_judge=rullet_ok(0)
    print(shoukin(rullet_judge,number,salary,2))
elif decide==1:
    rullet_judge=rullet_ok(1)
    print(shoukin(rullet_judge,number,salary,4))