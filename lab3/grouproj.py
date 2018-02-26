# import turtle
# import random #We'll need this later in the lab
# turtle.tracer(1,0) #This helps the turtle move more smoothly
# SIZE_X=800
# SIZE_Y=500
# turtle.setup(SIZE_X, SIZE_Y)
# turtle.bgcolor("blue")
# turtle.penup()
# SQUARE_SIZE = 20
# START_LENGTH = 2
# #Initialize lists
# pos_list = []
# stamp_list = []
# food_pos = []
# food_stamps = []
# #Set up positions (x,y) of boxes that make up the snake
# snake = turtle.clone()
# snake.shape("square")
# #Hide the turtle object (it's an arrow - we don't need to see it)
# turtle.hideturtle()

# for i in range(START_LENGTH):
#     x_pos=snake.pos()[0]
#     y_pos=snake.pos()[1]
#     x_pos+=SQUARE_SIZE

#     my_pos=(x_pos,y_pos)
#     snake.goto(x_pos,y_pos)
#     pos_list.append(my_pos)
#     stamp_list.append(snake.stamp())

# UP_ARROW="Up"
# LEFT_ARROW="Left"
# DOWN_ARROW="Down"
# TIME_STEP=100
# RIGHT_ARROW="Right"
# SPACEBAR="space"


# UP=0
# DOWN=1
# LEFT=2
# RIGHT=3

# turtle.register_shape("trash.gif")
# food = turtle.clone()
# food.shape("trash.gif")

# direction = UP

# UP_EDGE = 400
# DOWN_EDGE = -400
# RIGHT_EDGE = 650
# LEFT_EDGE = -650


# def up():
#     global direction#snake direction is global (same everywhere)
#     direction=UP #Change direction to up
#     #Update the snake drawing <- remember me later
#     print("You pressed the up key!")
# #2. Make functions down(), left(), and right() that change direction
# ####WRITE YOUR CODE HERE!!

# def down():
#     global direction
#     direction=DOWN
#     print("you pressed the down key")

# def left():
#     global direction
#     direction=LEFT
#     print("you pressed the left key")

# def right():
#     global direction
#     direction=RIGHT
#     print("you pressed the right key")
    
    
    
#  # Create listener for up key
# #3. Do the same for the other arrow keys
# ####WRITE YOUR CODE HERE!!
# turtle.listen()

# def make_food():
#     #The screen positions go from -SIZE/2 to +SIZE/2\
#     #But we need to make food pieces only appear on game squares
#     #So we cut up the game board into multiples of SQUARE_SIZE.
#     min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
#     max_x=int(SIZE_X/2/SQUARE_SIZE)-1
#     min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
#     max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
#     #Pick a position that is a random multiple of SQUARE_SIZE
#     food_x = random.randint(min_x,max_x)*SQUARE_SIZE
#     food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    
#     ##1.WRITE YOUR CODE HERE: ​ Make the food turtle go to the randomly-generated
#     ##                          position
#     random_pos=(food_x,food_y)
#     food.goto(food_x,food_y)
    
#     ##2.WRITE YOUR CODE HERE:Add the food turtle's position to the food positions list
#     food_pos.append(random_pos)
    
#     ##3.WRITE YOUR CODE HERE: ​ Add the food turtle's stamp to the food stamps list
#     stamp_id=food.stamp()
#     food_stamps.append(stamp_id)
    

# turtle.onkeypress(up, UP_ARROW)
# turtle.onkeypress(down,DOWN_ARROW)
# turtle.onkeypress(left,LEFT_ARROW)
# turtle.onkeypress(right,RIGHT_ARROW)
# turtle.listen()  


# def move_snake():
#     global food_stamps, food_pos
#     my_pos = snake.pos()
#     x_pos = my_pos[0]
#     y_pos = my_pos[1]
#     if direction==RIGHT:
#         snake.goto(x_pos + SQUARE_SIZE, y_pos)
#         print("You moved right!")
#     elif direction==LEFT:
#         snake.goto(x_pos - SQUARE_SIZE, y_pos)
#         print("You moved left!")
#     elif direction==UP:
#         snake.goto(x_pos, y_pos+SQUARE_SIZE)
#         print("you moved up")
#     elif direction==DOWN:
#         snake.goto(x_pos,y_pos-SQUARE_SIZE)
#         print("you moved down")

#     # make head
#     my_pos=snake.pos()
#     pos_list.append(my_pos)
#     new_stamp = snake.stamp()
#     stamp_list.append(new_stamp)
#     # make head
    
#     ######## SPECIAL PLACE - Remember it for Part 5
#     #pop zeroth element in pos_list to get rid of last the last
#     #piece of the tail

#     new_pos = snake.pos()
#     new_x_pos = new_pos[0]
#     new_y_pos = new_pos[1]
#     # The next three lines check if the snake is hitting the
#     # right edge.
#     if new_x_pos >= RIGHT_EDGE:
#         print("You hit the right edge! Game over!")
#         quit()
#     elif new_x_pos <= LEFT_EDGE:
#         print("you hit the left edge!Game over!")
#         quit()
#     elif new_y_pos >= UP_EDGE:
#         print("you hit the uper edge! Game over !")
#         quit()
#     elif new_y_pos <= DOWN_EDGE:
#         print("you hit the down edge! Game over !")
#         quit()
    




#     #If snake is on top of food item
#     if snake.pos() in food_pos:
#         food_ind=food_pos.index(snake.pos())#What does this do?
#         food.clearstamp(food_stamps[food_ind])#Remove eaten food
#         #stamp
#         food_pos.pop(food_ind)#Remove eaten food position
#         food_stamps.pop(food_ind)#Remove eaten food stamp
#         print("You have eaten the food!")
#         make_food()
#     else:
#          # remove tail
#         old_stamp = stamp_list.pop(0)
#         snake.clearstamp(old_stamp)
#         pos_list.pop(0)
#         # remove tail
#     #HINT: This if statement may be useful for Part 8
#     ...
#     #Don't change the rest of the code in move_snake() function:
#     #If you have included the timer so the snake moves
#     #automatically, the function should finish as before with a
#     #call to ontimer()
#     if snake.pos() in pos_list [0:-1]:
#         print(snake.pos())
#         print(pos_list)
#         print("game over")
#         quit()
        
        








    
#     turtle.ontimer(move_snake,TIME_STEP)

# make_food()
# move_snake()





# turtle.mainloop()		