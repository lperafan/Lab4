#TurtleGraphics.py
#Name:
#Date:
#Assignment:
    #drawPolygon(turtle, sides)
    #fillCorner(turtle, corner) 
    #squaresInSquares(turtle, num)

import turtle
hideturtle()

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for i in range (sides):
        bob.forward(50)
        bob.right(360/sides)
        
def fillCorner(alice, corner):
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()


def squaresInSquares(turtle, num):
    size = 100
    for _ in range(num):
        drawSquare(turtle, size)
        turtle.penup()
        turtle.goto(turtle.xcor() + 10, turtle.ycor() - 10)
        turtle.pendown()
        size -= 20

def main():
    myTurtle = turtle.Turtle()
    fillCorner(myTurtle, 1)
    myTurtle.penup()
    myTurtle.goto(-50, -50)
    myTurtle.pendown()
    squaresInSquares(myTurtle, 5)
    turtle.done()

main()
