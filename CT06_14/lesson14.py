# import turtle

# window = turtle.Screen()
# window.setup(width=600, height=400)
# animal = turtle.Turtle()
# animal.shape("turtle")
# animal.fillcolor("orange")
# window.mainloop()
# ## Task 3: Drawing
# Given the number of sides and each interior angle, draw each of the
# following shapes using a loop and the following functions:
#     .seth()
#     .up()
#     .down()
#     .forward()
#     .backward()
#     .left()
#     .right()

# **Task 3a**: Draw a line
# Number of sides: 1
# Interior angle: NA

# **Task 3b**: Draw a triangle
# Number of sides: 3
# Interior angle: 120

# **Task 3c**: Draw a square
# Number of sides: 4
# Interior angle: 90

# **Task 3d**: Draw a pentagon
# Number of sides: 5
# Interior angle: 72

# **Task 3e**: Draw a hexagon
# Number of sides: 6
# Interior angle: 60

# **Task 3f**: Draw a circle
# Number of sides: 360
# Interior angle: 1


# for animal in range(3):
#     animal.forward(100) 
#     animal.left(360/3)



# Task 1:

# import turtle

# window = turtle.Screen()
# window.setup(width=600, height=400)
# animal = turtle.Turtle()
# animal.shape("turtle")
# animal.fillcolor("green")
# animal.forward(100)
# window.mainloop()


# Task 2:

# import turtle

# window = turtle.Screen()
# window.setup(width=600, height=400)
# animal = turtle.Turtle()
# animal.shape("turtle")
# animal.fillcolor("green")


# # a
# # animal.forward(100)

# # b
# for i in range(3):
#     animal.forward(100)
#     animal.left(120)

# window.mainloop()

# import turtle

# window = turtle.Screen()
# window.setup(width=600, height=400)
# animal = turtle.Turtle()
# animal.shape("turtle")
# animal.fillcolor("green")
# animal.penup()
# animal.goto(x=-300,y=0)
# animal.pendown()
# animal.setx(x=300)
# animal.penup()
# animal.goto(x=0,y=200)
# animal.pendown()
# animal.sety(y=-200)
# window.mainloop()


# import turtle
# import random 

# window = turtle.Screen()
# window.setup(width=600, height=400)
# animal = turtle.Turtle()
# animal.shape("turtle")
# animal.fillcolor("green")


# for i in range(10):
#     x = random.randint(-280, 280)
#     y = random.randint(-280, 280)
#     animal.penup()
#     animal.goto(x,y)
#     animal.pendown()

#     for n in range(4):
#         animal.forward(5)
#         animal.left(90)

#     animal.penup()
#     animal.sety(y - 40)
#     animal.write(animal.pos(), align="center")

import random
import turtle

window = turtle.Screen()
window.setup(width=600, height=400)
animal = turtle.Turtle()
animal.shape("turtle")
animal.fillcolor("green")

x_limit = 180
y_limit = 180

animal.goto(-x_limit, -y_limit)

while True:
    if animal.xcor() < x_limit:
        animal.forward(1)
    animal.left(90)
    while animal.ycor() < y_limit:
        animal.forward(1)
    animal.left(90)
    while animal.xcor() > - x_limit:
        animal.forward(1)
    animal.left(90)
    while animal.ycor() >

# Task 6
# import turtle

# window = turtle.Screen()

# window.setup(width=400, height=400)

# t = turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("green")

# x_limit = 180
# y_limit = 180

# t.penup()

# t.goto(-x_limit, -y_limit) # Go to bottom left

# t.pendown()
# while True:
#     while t.xcor() < x_limit: # draw horizontal line towards the right
#         t.forward(1)
#     t.left(90)
#     while t.ycor() < y_limit: # draw vertical line upwards
#         t.forward(1)
#     t.left(90)
#     while t.xcor() > -x_limit: # draw horizontal line towards the left
#         t.forward(1)
#     t.left(90)
#     while t.ycor() > -y_limit: # draw vertical line downwards
#         t.forward(1)
#     t.left(90)

#     break
    
# window.mainloop()