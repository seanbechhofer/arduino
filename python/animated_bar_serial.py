# Reads csv data from the serial line and plots it on a bar chart,

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np
import time
import random
import serial
from sys import stdin

port = '/dev/cu.usbserial-AL00U1X7'
ser = serial.Serial(port, 9600)

def animated_barplot():
    stuff = ser.readline().split(",")
    print stuff
    data = []
    val = 0
    for st in stuff:
        try:
            val = int(st)
        except Exception, e:
            val = 0
        data.append(val)
    plt.xlim(-1,len(data)+1)
    plt.ylim(0, 1024)
    rects = plt.bar(range(len(data)), data,  align = 'center', color= 'b', alpha=0.4)
    fig.canvas.draw()
    
    while (True):
        stuff = ser.readline().split(",")
        data = []
        for st in stuff:
            try:
                val = int(st)
            except Exception, e:
                val = 0
            data.append(val)
        print ("tick")
        for rect, value in zip(rects,data):
            rect.set_height(int(value))
        fig.canvas.draw()

fig = plt.figure(figsize=(12,6))
win = fig.canvas.manager.window
win.after(100, animated_barplot)
plt.show()
