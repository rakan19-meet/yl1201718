from turtle import*
import turtle
import random
import math


class Ball(Turtle):
	def __init__ (self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.r  = r
		turtle.shape("circle")
		turtle.shapesize(r/10)
		turtle.color("red")

def move(self, screen_width, screen_hight):
	current_x = self.xcor()
	current_y = self.ycor()
	new_x = current_x + dx
	new_y = current_y + dy
	right_side_ball = new_x + r 
	left_side_ball = new_x - r 
	top_side_ball = new_x + r 
	bottom_side_ball = new_y - r 
	self.goto(new_x , new_y)
	if right_side_ball >= 300:
		new_x = current_x - new_x
		




def top(self):
	return.self.ycor()+0.5*self.h

def left(self):
	return.self.xcor()-0.5*self.w

def bottom(self):
	return.self.ycor()+0.5*self.h

def right(self):
	return.self.xxcor()-0.5*self.w

if (A.top() > B.bottom() and A.right() > B.left() and A.bottom() < B.top() and A.left() > B.right()):
	return true 













