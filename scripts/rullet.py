#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
import time

GPIO.setwarnings(False)
pin=[4,17,27,22]
StepCount = 8

def pin_init():
    Seq = list(range(0, StepCount))
    Seq[0] = [1,0,0,1]
    Seq[1] = [1,0,0,0]
    Seq[2] = [1,1,0,0]
    Seq[3] = [0,1,0,0]
    Seq[4] = [0,1,1,0]
    Seq[5] = [0,0,1,0]
    Seq[6] = [0,0,1,1]
    Seq[7] = [0,0,0,1]

    for i in range(0,4)
        GPIO.setup(pin[i], GPIO.OUT)
    
 def setStep(w1, w2, w3, w4):
    GPIO.output(pin[0], w1)
    GPIO.output(pin[1], w2)
    GPIO.output(pin[2], w3)
    GPIO.output(pin[3], w4)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def rullet():
    t=random.randint(0,360)
    d=360-t
    for i in range(3)
        forward(1,360)
    forward(1,t)
    time.sleep(4)
    forward(1,d)
    
    
if __name__ == '__main__':
    pin_init()
    rullet()
    