import turtle
from turtle import*
colormode(255)
import random
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)



class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle. __init__(self)
		self.width = width
		self.height = height
		turtle.register_shape("rectangle",((height,0),(height,width),(0,width),(0,0)))
		turtle.shape("rectangle")
		self.setheading(90)
class Square(Rectangle):
	def __init__(self,size):
		Rectangle.__init__(self,size,size)
	def random_color(self):
			
		self.shape("square")
		self.color(red,green,blue)
		print(red,green,blue)
turtle.speed(200)
class hexagon(Turtle):
	def __init__(self,size):
		Turtle. __init__(self)
		self.home()
		self.begin_poly()
		for i in range (6):
			self.fd(60)
			self.right(60)
		self.end_poly()
		p=self.get_poly()
		register_shape("reeko",p)
		self.shape("reeko")

boby=hexagon(5)
#rectangle123= rectangle(10,20)

turtle.mainloop()