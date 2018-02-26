from turtle import *
import turtle
import time
import random
from ball import *
turtle.colormode(255)
hideturtle()
tracer(0)
screen = turtle.Screen()
screen.bgpic('agario_background.gif')

number_of_balls = 8
minimum_ball_radius = 10
maximum_ball_radius = 40
minimum_ball_dx = -2
maximum_ball_dx = 2
minimum_ball_dy = -2
maximum_ball_dy = 2
balls =[]
score = 0
scoress = turtle.clone()

for i in range(number_of_balls):

	screen_random1_x = int(-screen_width+maximum_ball_radius)
	screen_random2_x = int(screen_width-maximum_ball_radius)
	random_x = random.randint(screen_random1_x,screen_random2_x)
	
	screen_random1_y = int(-screen_height+maximum_ball_radius)
	screen_random2_y = int(screen_height-maximum_ball_radius)
	random_y = random.randint(screen_random1_y,screen_random2_y)
	
	random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	while random_dx == 0:
		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)

	random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	while random_dy == 0:
		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	radius = random.randint(minimum_ball_radius,maximum_ball_radius)

	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	


	ball = Ball(random_x,random_y,random_dx,random_dy,radius,color)
	balls.append(ball)


def move_all_balls():
	for variable in range(number_of_balls):
		balls[variable].move(screen_width,screen_height)

def check_collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False					
	balls_distance = ((ball_a.xcor()-ball_b.xcor())**2 +(ball_a.ycor()-ball_b.ycor())**2)**0.5
	if balls_distance+10 <= ball_a.r+ball_b.r:
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in balls:
		for ball_b in balls:
			if check_collide(ball_a,ball_b) == True:
				radius1 = ball_a.r
				radius2 = ball_b.r
				random_x = random.randint(screen_random1_x,screen_random2_x)
				random_y = random.randint(screen_random1_y,screen_random2_y)
				random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
				while random_dx == 0:
					random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
				random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
				while random_dy == 0:
					random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
				radius = random.randint(minimum_ball_radius,maximum_ball_radius)
				color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

				if radius1 > radius2:
					ball_b.goto(random_x,random_y)
					ball_b.dx = random_dx
					ball_b.dy = random_dy
					ball_b.r = radius
					ball_b.shapesize(ball_b.r/10)
					ball_b.color = color
					ball_a.r += 0.5
					ball_a.shapesize(ball_a.r/10)
					
				elif radius1 < radius2:
					ball_a.goto(random_x,random_y)
					ball_a.dx = random_dx
					ball_a.dy = random_dy
					ball_a.r = radius
					ball_a.shapesize(ball_a.r/10)
					ball_a.color = color
					ball_b.r += 0.5
					ball_b.shapesize(ball_b.r/10)
					
def check_myball_collision():	
	global score , scoress, maximum_ball_radius		
	for ball in balls:
		random_x = random.randint(screen_random1_x,screen_random2_x)
		random_y = random.randint(screen_random1_y,screen_random2_y)
		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		while random_dx == 0:
			random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		while random_dy == 0:
			random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		radius = random.randint(minimum_ball_radius,maximum_ball_radius)
		color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		if check_collide(MY_BALL,ball) == True:
			radius3 = MY_BALL.r
			radius4 = ball.r

			



			if MY_BALL.r < ball.r:
				print("Game Over bb!!")
				return 	False

					
			else:
				MY_BALL.r += 2
				maximum_ball_radius += 4
				MY_BALL.shapesize(MY_BALL.r/10)
				score += 1
				scoress.pu()
				scoress.goto(0,250)
				scoress.clear()

				scoress.write("score: " + str(score),align="center",font=("Arial", 20, "bold"))
				ball.goto(random_x,random_y)
				ball.dx = random_dx
				while ball.dx == 0:
					ball.dx = random.randint(minimum_ball_dx,maximum_ball_dx)
				ball.dy = random_dy
				while ball.dy == 0:
					ball.dy = random.randint(minimum_ball_dy,maximum_ball_dy)
				ball.r = radius
				ball.shapesize(ball.r/10)
				ball.color = color
	return True

def movearound(event):
	X1 = event.x - screen_width
	Y1 = screen_height - event.y
	MY_BALL.goto(X1,Y1)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while running == True:
	if screen_width !=  int(turtle.getcanvas().winfo_width()/2) or screen_height != int(turtle.getcanvas().winfo_height()/2):
		screen_width =int(turtle.getcanvas().winfo_width()/2)
		screen_height = int(turtle.getcanvas().winfo_height()/2)
	move_all_balls()
	check_all_balls_collision()
	if check_myball_collision() == False:
		turtle.goto(0,0)
		turtle.color("pink")		
		turtle.write("Game Over bb!!",font=("Arial", 50, "bold",),align="center")
		time.sleep(4)
		turtle.bye()
	getscreen().update()
	time.sleep(sleep)
turtle.mainloop()
