from turtle import *

# Draw a square centered on the screen
# move into position
up()
forward(50)
left(90)
forward(50)
left(90)

down()


# Draw a square
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)


# Draw a circle on an orange background
pencolor('orange')
width(10)
circle(180)


# Draw a star

for i in range(5):
    forward(100)
    right(144)

mainloop()
