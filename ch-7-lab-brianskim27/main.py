import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    
    while(n != 1):

        if(n % 2) == 0:        # n is even
            n = n // 2
            count += 1
        else:                 # n is odd
            n = n * 3 + 1
            count += 1
    
    return count

def Graph(upper):
    writer = turtle.Turtle()
    grapher = turtle.Turtle()
    
    window = turtle.Screen()
    window.reset()
    window.setworldcoordinates(0, 0, 10, 10)

    max_so_far = 0

    for i in range(1, upper + 1):
        result = seq3np1(i)

        if result > max_so_far:
            max_so_far = result
        
        window.setworldcoordinates(0, 0, i + 10, max_so_far + 10)
        
        writer.clear()
        writer.up()
        writer.goto(0, max_so_far)
        writer.down()
        writer.hideturtle()
        
        writer.write(f"Maximum so far: {i}, {max_so_far}", font = ('Arial', 12, 'normal'))
        grapher.goto(i, max_so_far)
        grapher.dot()

    window.exitonclick()
        
def main():
    start = int(input("What is the upper bound? "))
    
    if start < 0:
        quit()

    else:
        for i in range(1, start + 1):         #Part A
            print("Iteration:", i)
            print("Count:", seq3np1(i))
        
        Graph(start)                          #Part B

main()