from tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
servoX = 
servoY = 

p = GPIO.PWM(27,50)
p.start(7.5)




HEIGHOFSCREEN = 600
WIFTHOFSCREEN = 600

def moveServo():



def convertPWM(x,y):
    pwmX = 2.5+(x/(WIFTHOFSCREEN/10))
    pwmY = 2.5+(y/(HEIGHOFSCREEN/10))
    print(pwmX, pwmY)
    
def event(event):
    x, y = event.x, event.y
    convertPWM(x,y)

def main():
    root = Tk()
    window = Canvas(root, width=WIFTHOFSCREEN, height=HEIGHOFSCREEN, bg='gray')
    window.pack()

    #calls event and bindings
    #<b1-motion> required you to hold down the mouse bottom
    #https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
    root.bind("<Motion>", event)

    #1000ms after calling the mainloop(), call main
    #root.after(1000, main)
    root.title("Make a move on Me! ;)")

    root.mainloop()

if __name__ == "__main__":
    main()




