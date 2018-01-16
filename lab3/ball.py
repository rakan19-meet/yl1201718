from turtle import*
import turtle
import random
import math

RUNNING = True
SLEEP = 0.0077
screen_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2


class Ball(Turtle):
	def __init__ (self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
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
	
	

	if right_side_ball > 300:
		new_x = current_x - new_x
	
	elif bottom_side_ball < -300:
		new_y = current_y + dy

	elif left_side_ball < -300:
		new_x = current_x + dx

	elif right_side_ball > 300:
		new_x = current_x - dx



#def top(self):
#	return.self.ycor()+(0.5*self.height)



#def bottom(self):
#	return.self.ycor()-(0.5*self.height)

#def right(self):
#	return.self.xcor()+(0.5*self.width)
#def left(self):
#	return.self.xcor()-(0.5*self.width)

# if (A.top() > B.bottom() and A.right() > B.left() and A.bottom() < B.top() and A.left() > B.right()):
#	return true 

my_ball = Ball(100,0,5,5,10,"red")
my_ball.goto(10,10)
my_ball.ht()
mainloop()









