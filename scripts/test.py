#!/usr/bin/python3
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Int32
rospy.init_node('sevice_client1')
pub=rospy.Publisher('rullette_judge',Int32,queue_size=2)
rate=rospy.Rate(10)
for i in range(3):
  pub.publish(1)
  rate.sleep()
