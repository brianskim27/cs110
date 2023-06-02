class Rectangle:
    def __init__(self, x, y, h, w):
        """
        Creates the instance variables and sets any negative value to 0.
        args: self.x (int) The instantiated variable for the x value of the rectangle.
        self.y (int) The instantiated variable for the y value of the rectangle.
        self.height (int) The instantiated variable for the height of the rectangle.
        self.width (int) The instantiated variable for the width of the rectangle.
        dimensions (tuple) Sets any of the rectangle dimensions to 0 if they are negative.
        dimension_2 (list) The new set of values for self.x, self.y, self.height, and self.width.
        return: None
        """
        self.x = x
        self.y = y
        self.height = h
        self.width = w

        dimensions = (self.x, self.y, self.height, self.width)
        dimensions_2 = [0 if i < 0 else i for i in dimensions]
        (self.x, self.y, self.height, self.width) = dimensions_2

    def __str__(self):
        """
        Gives the values of each dimension of the rectangle (x, y, width, height).
        args: None
        return: A string consisted of the values of self.x, self.y, self.width, and self.height.
        """
        return f"(x: {self.x}, y: {self.y}) width: {self.width}, height: {self.height}"