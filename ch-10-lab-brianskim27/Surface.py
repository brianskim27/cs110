from Rectangle import Rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
        """
        Creates instance variables for the rectangle and image that are used.
        args: self.rect (class) The rectangle object with dimensions x, y, h, and w.
        self.image (str) The name of the image file.
        return: None
        """
        self.rect = Rectangle(x, y, h, w)
        self.image = str(filename)

    def getRect(self):
        """
        Gives the values/dimensions of the rectangle.
        args: None
        return: self.rect - the rectangle object
        """
        return self.rect
