from tkinter import *
root = Tk()

HEIGHOFSCREEN = 600
WIFTHOFSCREEN = 600

window = Canvas(root, width=WIFTHOFSCREEN, height=HEIGHOFSCREEN, bg='gray')
window.pack()

def convertPWM(x,y):
    pwmX = 2.5+(x/(WIFTHOFSCREEN/10))
    pwmY = 2.5+(y/(HEIGHOFSCREEN/10))
    print(pwmX, pwmY)
    
def event(event):
    x, y = event.x, event.y
    convertPWM(x,y)

def main():
    print("Bruce")

#calls event and bindings
#<b1-motion> required you to hold down the mouse bottom
#https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
root.bind("<Motion>", event)


#1000ms after calling the mainloop(), call main
root.after(1000, main)
root.title("Make a move on Me! ;)")

root.mainloop()
