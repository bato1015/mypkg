#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import rospy
from std_msgs.msg import Int32

angleCount=2


angle = list(range(0, angleCount))
angle[1]=[0,1,2,3]
angle[0]=[0,1,0,1]

def select(ration):
    if(ration==2):
        number=int(input("0~1?"))
    elif(ration==4):
        number=int(input("0~3?"))
    return number
   

def random_num(ration):
    count=random.randint(0,3)
    if(ration==2):
        return angle[0][count]
    elif(ration==4):
        return angle[1][count]

def judge(twice,salary,ru_num,user_num):
    if ru_num==user_num:
        return twice*salary
    else:
        return 0

def win_judge(money):
    if money!=0:
        str1="hit"
        return str1
    else:
        str1="down"
        return str1
if __name__ == '__main__': 
   rospy.init_node('sevice_client')
   pub=rospy.Publisher('rullette_judge1',Int32,queue_size=1)
   rate=rospy.Rate(10)

   ration = int(input("2?4?"))
   salary= int(input("money?"))
   user_num=select(ration)
   ru_num=random_num(ration)
   money=judge(ration,salary,ru_num,user_num)
   print(ration,salary,user_num,ru_num,money)
   for i in range(1):
       pub.publish(ru_num)
       rate.sleep()
