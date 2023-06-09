'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle, width, top_left_x, top_left_y) - to outline dartboard
  drawLine(myturtle, x_start, y_start, x_end, y_end) - to draw axes
  drawCircle(myturtle, radius) - to draw the circle
  setUpDartboard(myscreen, myturtle) - to set up the board using the above functions
  isInCircle(myturtle, circle_center_x, circle_center_y, radius) - determine if dot is in circle
  throwDart(myturtle)
  playDarts(myturtle) - a simulated game of darts between two players
  montePi(myturtle, num_darts) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
def drawSquare(myturtle, width, top_left_x, top_left_y):
  myturtle.up()
  myturtle.goto(top_left_x, top_left_y)
  myturtle.down()
  
  for i in range(4):
    myturtle.forward(width)
    myturtle.right(90)

def drawLine(myturtle, x_start, y_start, x_end, y_end):
  myturtle.up()
  myturtle.goto(x_start, y_start)
  myturtle.down()
  myturtle.goto(x_end, y_end)

def drawCircle(myturtle, radius):
  myturtle.up()
  myturtle.goto(0,-1)
  myturtle.down()
  myturtle.circle(radius)

def setUpDartboard(screen, myturtle):
  screen.reset()
  screen.setworldcoordinates(-1, -1, 1, 1)
  
  drawSquare(myturtle, 2, -1, 1)
  drawLine(myturtle, -1, 0, 1, 0)
  drawLine(myturtle, 0, -1, 0, 1)
  drawCircle(myturtle, 1)

def throwDart(myturtle):
  myturtle.up()
  myturtle.goto(random.uniform(-1, 1), random.uniform(-1, 1))
  myturtle.down()
  
  if isInCircle(myturtle, 0, 0, 1) == True:
    myturtle.dot("blue")
  
  if isInCircle(myturtle, 0, 0, 1) == False:
    myturtle.dot("red")

def isInCircle(myturtle, circle_center_x, circle_center_y, radius):
  if myturtle.distance(circle_center_x, circle_center_y) == radius:
    return True
  
  elif myturtle.distance(circle_center_x, circle_center_y) <= radius:
    return True
  
  else:
    return False

def playDarts(myturtle):
  player_1 = 0
  player_2 = 0 

  for i in range(10):
    throwDart(myturtle)

    if isInCircle(myturtle, 0, 0, 1) ==  True:
      player_1 += 1

    throwDart(myturtle)
    
    if isInCircle(myturtle, 0, 0, 1) == True:
      player_2 += 1

  if player_1 == player_2:
    print("Tie! Both players scored:", player_1)
  
  elif player_1 > player_2:
    print("Player 1 wins with a score of:", player_1)
  
  else:
    print("Player 2 wins with a score of:", player_2)
  
def montePi(myturtle, num_darts):
  inside_count = 0
  
  for i in range(num_darts):
    
    throwDart(myturtle)
    
    if isInCircle(myturtle, 0, 0, 1) == True:
      inside_count += 1
  
  approx = (inside_count / num_darts) * 4
  return(approx)



#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()