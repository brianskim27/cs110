import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def setupWindow(screen_object):
    screen_object = turtle.Screen()
    screen_object.reset()
    screen_object.setworldcoordinates(math.radians(-360),-1,math.radians(360),1)
    screen_object.bgcolor("light blue")

def setupAxis(turtle_object):
    turtle_object.up()
    turtle_object.goto(math.radians(-360),0)
    turtle_object.down()
    turtle_object.goto(math.radians(360),0)
    
    turtle_object.up()
    turtle_object.goto(0,-1)
    turtle_object.down()
    turtle_object.goto(0,1)
    
    turtle_object.up()
    turtle_object.goto(math.radians(-360),0)
    turtle_object.down()

def drawSineCurve(turtle_object):
    x = -360
    y = math.sin(math.radians(x))
    print(x,y)
    
    turtle_object.color("red")
    turtle_object.goto(math.radians(x),y)
    
    for x in range(-360,361):
        y = math.sin(math.radians(x))
        turtle_object.goto(math.radians(x),y)
        print(x,y)
    
    turtle_object.up()
    turtle_object.goto(math.radians(-360),1)
    turtle_object.down()

def drawCosineCurve(turtle_object):
    x = -360
    y = math.cos(math.radians(x))
    print(x,y)
    
    turtle_object.color("blue")
    turtle_object.goto(math.radians(x),y)
    
    for x in range(-360,361):
        y = math.cos(math.radians(x))
        turtle_object.goto(math.radians(x),y)
        print(x,y)
    
    turtle_object.up()
    turtle_object.goto(math.radians(-360),0)
    turtle_object.down()

def drawTangentCurve(turtle_object):
    x = -360
    y = math.tan(math.radians(x))
    print(x,y)
    
    turtle_object.color("green")
    turtle_object.goto(math.radians(x),y)
    
    for x in range(-360,361):
        y = math.tan(math.radians(x))
        turtle_object.goto(math.radians(x),y)
        print(x,y)

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
