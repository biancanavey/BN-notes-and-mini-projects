# Let's draw some cool drawings with the package tutrle

# Import turtle
import turtle

# Let's get a nice set up in turtle

turtle.bgcolor('Yellow')  # Background color
turtle.pensize(2)  # Pen size
turtle.color('Green')

# Draw a square
# turtle.forward(50)  # Moves forward
# turtle.left(90)  # Moves left 90 degrees
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.done()  # Allows turtle to stay on the screen

# Pattern
# for colours in ['black','green','red','blue','white']:
#     turtle.color(colours)
#     turtle.circle(150)
#     turtle.left(60)
# turtle.done()

# Lets make a loop in a loop
for i in range(6):
    for colours in ['black', 'green', 'red', 'blue', 'white']:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
turtle.done()
