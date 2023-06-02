import turtle
import random

#Part A
START_X = -150
START_Y1 = 20
START_Y2 = -20

class TurtleRace:
    def __init__(self, turtle_1, turtle_2, min, max):   
        """
        Initialize the variables that will be used.
        args: turtle_1 (turtle) One of the turtles that will be racing.
        turtle_2 (turtle) The other turtle that will be racing.
        min (int) The minimum distance that the turtles will move.
        max (int) The maximum distance that the turtles will move.
        return: None
        """
        self.turtle_1 = turtle_1
        self.turtle_2 = turtle_2
        
        self.min = min
        self.max = max
        
        self.distance_1 = 0
        self.distance_2 = 0

    def racers(self):
        """
        Create two turtles and move them to their starting positions.
        args: 'orange' (string) Color of turtle_1.
        'blue' (string) Color of turtle_2.
        'turtle' (string) Shape of the turtles.
        START_X (int) Starting x-coordinate of the turtles.
        START_Y1 (int) Starting y-coordinate of turtle_1.
        START_Y2 (int) Starting y-coordinate of turtle_2.
        return: None
        """
        self.turtle_1.color('orange')
        self.turtle_1.shape('turtle')
        
        self.turtle_2.color('blue')
        self.turtle_2.shape('turtle')
    
        self.turtle_1.up()
        self.turtle_1.goto(START_X, START_Y1)

        self.turtle_2.up()
        self.turtle_2.goto(START_X, START_Y2)

    def singleCall(self):
        """
        Move each turtle forward once by a random distance between two numbers (min, max).
        args: distance (int) A random value between two numbers (min, max).
        self.min (int) The minimum value the distance can be.
        self.max (int) The maximum value the distance can be.
        START_X (int) Starting x-coordinate of the turtles.
        START_Y1 (int) Starting y-coordinate of turtle_1.
        START_Y2 (int) Starting y-coordinate of turtle_2.
        return: None
        """
        distance = random.randrange(self.min, self.max)    
        self.turtle_1.forward(distance)
        
        distance = random.randrange(self.min, self.max)
        self.turtle_2.forward(distance)
        
        self.turtle_1.goto(START_X, START_Y1)
        self.turtle_2.goto(START_X, START_Y2)

    def multipleCalls(self, num_calls):
        """
        Move each turtle forward num_calls times by a random distance between two numbers (min, max).
        args: num_calls (int) Number of times the turtles will move forward.
        distance (int) A random value between two numbers (min, max).
        self.min (int) The minimum value the distance can be.
        self.max (int) The maximum value the distance can be.
        START_X (int) Starting x-coordinate of the turtles.
        START_Y1 (int) Starting y-coordinate of turtle_1.
        START_Y2 (int) Starting y-coordinate of turtle_2.
        return: None
        """
        for i in range(num_calls):                           #The turtles move forward by a random distance an assigned number of times.
            distance = random.randrange(self.min, self.max)
            self.turtle_1.forward(distance)
            distance = random.randrange(self.min, self.max)
            self.turtle_2.forward(distance)
        
        self.turtle_1.goto(START_X, START_Y1)
        self.turtle_2.goto(START_X, START_Y2)
        print("The turtles will now go back to their starting positions.")

    def race(self, num_calls):
        """
        Move each turtle forward num_calls times by a random distance between two numbers (min, max) and store the total distances.
        args: num_calls (int) Number of times the turtles will move forward.
        distance (int) A random value between two numbers (min, max).
        self.distance_1 (int) Distance that turtle_1 has moved so far.
        self.distance_2 (int) Distance that turtle_2 has moved so far.
        self.min (int) The minimum value the distance can be.
        self.max (int) The maximum value the distance can be.
        START_X (int) Starting x-coordinate of the turtles.
        START_Y1 (int) Starting y-coordinate of turtle_1.
        START_Y2 (int) Starting y-coordinate of turtle_2.
        """
        for i in range(num_calls):                          #The turtles move forward by a random distance an assigned number of times, and the total distance is stored.
            distance = random.randrange(self.min, self.max)
            self.turtle_1.forward(self.distance_1)
            self.distance_1 += distance
            
            distance = random.randrange(self.min, self.max)
            self.turtle_2.forward(self.distance_2)
            self.distance_2 += distance
        
        self.turtle_1.goto(START_X, START_Y1)
        self.turtle_2.goto(START_X, START_Y2)

        return self.distance_1, self.distance_2

# Part B - complete part B here
    def drawEquilateralTriangle(self, distance):
        """
        Draw an equilateral triangle with a length of distance.
        args: distance (int) An assigned value for the length of each side of the shape.
        360/3 (int) The degree of each angle of the shape.
        return: None
        """
        self.turtle_1.hideturtle()
        self.turtle_2.down()
        angle = 360/3

        print("Now drawing an equilateral triangle.")

        for i in range(3):
            self.turtle_2.forward(distance)
            self.turtle_2.left(angle)
        
        self.turtle_2.clear()

    def drawSquare(self, distance):
        """
        Draw a square with a length of distance.
        args: distance (int) An assigned value for the length of each side of the shape.
        360/4 (int) The degree of each angle of the shape.
        return: None
        """
        self.turtle_1.hideturtle()
        self.turtle_2.down()
        angle = 360/4

        print("Now drawing a square.")

        for i in range(4):
            self.turtle_2.forward(distance)
            self.turtle_2.left(angle)
        
        self.turtle_2.clear()
    
    def drawHexagon(self, distance):
        """
        Draw a hexagon with a length of distance.
        args: distance (int) An assigned value for the length of each side of the shape.
        360/6 (int) The degree of each angle of the shape.
        return: None
        """
        self.turtle_1.hideturtle()
        self.turtle_2.down()
        angle = 360/6

        print("Now drawing a hexagon.")

        for i in range(6):
            self.turtle_2.forward(distance)
            self.turtle_2.left(angle)
        
        self.turtle_2.clear()

    def drawNonagon(self, distance):
        """
        Draw a nonagon with a length of distance.
        args: distance (int) An assigned value for the length of each side of the shape.
        360/9 (int) The degree of each angle of the shape.
        return: None
        """
        self.turtle_1.hideturtle()
        self.turtle_2.down()
        angle = 360/9

        print("Now drawing a nonagon.")

        for i in range(9):
            self.turtle_2.forward(distance)
            self.turtle_2.left(angle)
        
        self.turtle_2.clear()

    def drawDodecagon(self, distance):
        """
        Draw a dodecagon with a length of distance.
        args: distance (int) An assigned value for the length of each side of the shape.
        360/12 (int) The degree of each angle of the shape.
        return: None
        """
        self.turtle_1.hideturtle()
        self.turtle_2.down()
        angle = 360/12

        print("Now drawing a dodecagon.")

        for i in range(12):
            self.turtle_2.forward(distance)
            self.turtle_2.left(angle)
        
        self.turtle_2.clear()

    def drawShapes(self, num_sides, distance): 
        """
        Draw a polygon with a num_sides number of sides with a length of distance.
        args: distance (int) An assigned value for the length of each side of the shape.
        angle (int) The degree of each angle of the shape.
        return: None
        """
        self.turtle_1.hideturtle()
        self.turtle_2.down()
        angle = 360/num_sides

        print(f"Now drawing a polygon with {num_sides} sides.")

        for i in range(num_sides):
            self.turtle_2.forward(distance)
            self.turtle_2.left(angle)
            
        self.turtle_2.clear()

def main():
    min = int(input("What is the minimum distance that the racers can move? "))
    print(f"The shortest distance the turtles can move is {min} step.")
    max = int(input("What is the maximum distance that the racers can move? "))
    print(f"The longest distance the turtles can move is {max} steps.")
    
    window = turtle.Screen()
    window.bgcolor('lightblue')
    
    michelangelo = turtle.Turtle()
    leonardo = turtle.Turtle()
    
    turtle_race = TurtleRace(michelangelo, leonardo, min, max)
    
    turtle_race.racers()

    distance_turtle_1, distance_turtle_2 = turtle_race.race(10)
    print("Distance michelangelo traveled:", distance_turtle_1, "\nDistance leonardo traveled:", distance_turtle_2)
    
    if distance_turtle_1 > distance_turtle_2:
        print("michelangelo is the winner!")
    elif distance_turtle_1 < distance_turtle_2:
        print("leonardo is the winner!")
    
    turtle_race.drawEquilateralTriangle(100)
    turtle_race.drawSquare(100)
    turtle_race.drawHexagon(100)
    turtle_race.drawNonagon(100)
    turtle_race.drawDodecagon(100)
    
    num_sides = int(input("How many sides do you want your shape to have? "))
    turtle_race.drawShapes(num_sides, 100)

    window.exitonclick()

main()