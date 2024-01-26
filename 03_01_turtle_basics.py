from turtle import Turtle, Screen

# Create screen setup Turtle
screen = Screen()
donatello = Turtle(shape="turtle")
donatello.shapesize(2)
donatello.pensize(5)
donatello.speed(1)

# Move turtle around on screen
donatello.forward(100)
donatello.left(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(200)

# Click to exit 
screen.exitonclick()