import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

n = random.randrange(1,100)      #Method 1 - single call to forward the turtles
michelangelo.forward(n)
n = random.randrange(1,100)
leonardo.forward(n)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(10):              #Method 2 - 10 calls to forward the turtles
    n = random.randrange(1,10)
    michelangelo.forward(n)
    n = random.randrange(1,10)
    leonardo.forward(n)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
# michelangelo.up()
# leonardo.down()

# for i in range(3):                #equilateral triangle
#     leonardo.forward(100)
#     leonardo.left(120)
# leonardo.clear()

# for i in range(4):                #square
#     leonardo.forward(100)
#     leonardo.left(90)
# leonardo.clear()

# for i in range(6):                #hexagon
#     leonardo.forward(100)
#     leonardo.left(60)
# leonardo.clear()

# for i in range(9):                #nonagon
#     leonardo.forward(100)
#     leonardo.left(40)
# leonardo.clear()

# for i in range(12):               #dodecagon 
#     leonardo.forward(100)
#     leonardo.left(30)
# leonardo.clear()

window.exitonclick()
