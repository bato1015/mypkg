#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32


rospy.init_node('sevice_client')

def shoukinn(a,b,c,d):
    if a==b:
        return c*d
    else:
        return 0
def number(rullet_num):
    print(rullet_num)

pub=rospy.Publisher('rullette_judge',Int32,queue_size=1)
rate=rospy.Rate(1)
#decide = input("0:2倍？ 1:4倍?")
decide=0
#salary= input("いくらかける?")
#number=input("何番?")

pub.publish(decide)
rate.sleep()
sub=rospy.Subscriber('rulette_result',Int32,number)

if decide==0:
    print("2倍")
elif decide==1:
    print("4倍")
#if __name__ == '__main__': 
   # pub.publish(decide)
