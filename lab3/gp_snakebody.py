from turtle import *
import turtle
import time
import random
colormode(255)
hideturtle()
tracer(0)

# def movearound(event):
# 	MY_BALL.goto(event.x- screen_width, -screen_height+100)
# turtle.getcanvas().bind("<Motion>", movearound)
# turtle.getscreen().listen()
turtle.pu()



FIXED_RADUIS = 1
FIXED_COLOR="blue"
game = True
screen_width = 350
screen_height = 0
class head_circle(Turtle):
	def __init__ (self,color,x,y,radius):
		Turtle.__init__(self)
		self.color = color
		self.shape("circle")
		self.shapesize(radius)
		self.tails=[]

	def add_tail():
		newtail = tail_circle()
		self.tails.append(newtail)

	def move(self,width,height):
		current_x = self.xcor()
		new_x = current_x + self.dx 
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		# top_side_ball = new_y + self.r
		# bottom_side_ball = new_y - self.r
		self.goto(new_x,self.y)

		# if top_side_ball > height:
		# 	self.dy = - self.dy

		# elif bottom_side_ball < -height:
		# 	self.dy = -self.dy

		if left_side_ball < -width:
			print("l.border")

		elif right_side_ball > width:
			print("r.border")

	
MY_HEAD = head_circle(FIXED_COLOR, 0 , 0 , FIXED_RADUIS)
# head_circle = Ball 
# tt = head_circle(FIXED_COLOR,0,0,FIXED_RADUIS)


class tail_circle(Turtle):
	def __init__ (self,color,radius):
		self.color = color
		self.shape("circle")
		self.shapesize(radius)

	def maketail():
		pass

def movearound(event):
	X1 = event.x - screen_width
	Y1 = screen_height - event.y
	MY_HEAD.goto(X1,0)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while game == True:
	# movearound()
	turtle.getscreen().update()



	
turtle.mainloop()












