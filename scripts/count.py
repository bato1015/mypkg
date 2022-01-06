#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
form mypkg.srv import color colorResponse
import RPi.GPIO as GPIO
import time

def roulette_init_sever():
    forward(1 / 1000.0, 360)
    rospy.init_node('roulette_color',anonymous=True)
    pub=rospy.Service('roulette_color',color, color_q)
    rospy.spin()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 4 # pink
coil_A_2_pin = 17 # orange
coil_B_1_pin = 27 # blue
coil_B_2_pin = 22 # yellow
 
# adjust if different
StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [1,0,0,1]
Seq[1] = [1,0,0,0]
Seq[2] = [1,1,0,0]
Seq[3] = [0,1,0,0]
Seq[4] = [0,1,1,0]
Seq[5] = [0,0,1,0]
Seq[6] = [0,0,1,1]
Seq[7] = [0,0,0,1]


GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
def color_q(rew):
    re=3
    return re
 
if __name__ == '__main__':
    roulette_init_sever()
