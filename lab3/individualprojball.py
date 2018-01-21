from turtle import*
import time
import random
from ball import*
#turtle.tracer(0)
#ht()

RUNNING = True 
SLEEP = 0.0077

SCREEN_WIDTH =int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
my_ball = Ball (0,0,5,5,10,"red")
BALLS = []

for i in range(NUMBER_OF_BALLS):
	x = random.randint (-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint (-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint (MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	if dx == 0:
		dx += 1
	dy = random.randint (MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	if dy == 0:
		dy += 1	
	radius = random.randint (MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

ball = Ball(x,y,dx,dy, radius, color)
BALLS.append(ball)


def move_all_BALLS():
	for variable in range(NUMBER_OF_BALLS):
		BALLS[variable].move(SCREEN_WIDTH,SCREEN_HEIGHT)

for i in range (100):
	move_all_BALLS()		

def check_collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False

	BALLS_distance = ((ball_A.xcor()-ball_b.xcore())^2+(ball_a.ycor())^2)^0.5

def check_all_BALLS_collision():
	for ball_a in range (BALLS):
		for ball_b in range (BALLS):	
			if check_collide == True:
				radius1 = ball_a.r
				radius2 = ball_b.r
				if radius1 > radius2:
					ball.b = ball(x,y,dx,dy,radius,color)
					radius1 += 1
				elif radius1 < radius2:
					ball.a = ball(x,y,dx,dy,radius,color)
					radius2 += 1






mainloop()