import pygame
import random
from src import hero
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        """
        Initializes the inputs and variables in use
        args: self.image (image) Image of the enemy
        self.rect (rect) Image of the enemy as a rectangle
        self.rect.x (int) X coordinate of the enemy
        self.rect.y (int) Y coordinate of the enemy
        self.name (str) Name of the enemy
        self.pixel (int) Size of the enemy
        self.height (int) Height of the screen
        self.width (int) Width of the screen
        return: None
        """
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        
        self.pixel = 95
        self.height = 480
        self.width = 640

    def update(self):
        """
        Creates boundaries for the screen that the enemies cannot move past
        args: self.rect.x (int) X coordinate of the enemy
        self.rect.y (int) Y coordinate of the enemy
        self.pixel (int) Size of the enemy
        return: None
        """
        if self.rect.x + self.pixel >= self.width:
            self.rect.x += -1
        
        elif self.rect.x <= 0:
            self.rect.x += 1
        
        elif self.rect.y + self.pixel >= self.height:
            self.rect.y += -1

        elif self.rect.y <= 0:
            self.rect.y += 1
        
        else:
            self.rect.x += random.randrange(-1, 2)
            self.rect.y += random.randrange(-1, 2)
            
            #Testing the boundaries
            # self.rect.x += 1
            # self.rect.x += -1
            # self.rect.y += 1 
            # self.rect.y += -1
