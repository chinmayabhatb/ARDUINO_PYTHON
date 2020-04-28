import serial
import time
from tkinter import *


def led_on():
     arduinoData.write(b'1')
     print("LED IS ON")

def led_off():
     arduinoData.write(b'0')
     print("LED IS OFF")

led_control_window= Tk()
led_control_window.geometry("200x200")
btn=Button(led_control_window,text="led on",command=led_on,width="200",height="5")
btn2=Button(led_control_window,text="led off",command=led_off,width="200",height="5")
btn.pack()
btn2.pack()
arduinoData = serial.Serial('com3',9600)
