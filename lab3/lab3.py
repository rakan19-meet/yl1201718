import turtle
turtle.speed(100)
turtle.pensize(1)
b=1
angle=369/b
turtle.tracer(1000)
for i in range(int (angle)):
	turtle.right(b)
	turtle.forward(200)
	turtle.right(45)
	turtle.forward(100)
	turtle.right(85)
	turtle.forward(55)
	turtle.home()
	b+=1
turtle.mainloop()
	

	
