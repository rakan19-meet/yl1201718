from turtle import*
import turtle
import random
import time



def click(x,y):
    turtle.SetCursorPos((x,y))
    turtle.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    turtle.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
click(10,10)

turtle.mainloop()
