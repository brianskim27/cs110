import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        """
        Initializes the inputs and variables in use
        args: self.image (image) Image of the hero
        self.rect (rect) Image of the hero as a rectangle
        self.rect.x (int) X coordinate of the hero
        self.rect.y (int) Y coordinate of the hero
        self.name (str) Name of the hero
        self.speed (int) The speed of the hero
        return: none
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
        self.name = name
        self.speed = 3
        self.health = 3

    #methods to make moving our hero easier
    def move_up(self):
        """
        Sets up the ability for the hero to move up
        args: self.rect.y (int) The y coordinate of the hero
        self.speed (int) The speed of the hero
        return: none
        """
        self.rect.y -= self.speed
    def move_down(self):
        """
        Sets up the ability for the hero to move down
        args: self.rect.y (int) The y coordinate of the hero
        self.speed (int) The speed of the hero
        return: none
        """
        self.rect.y += self.speed
    def move_left(self):
        """
        Sets up the ability for the hero to move left
        args: self.rect.x (int) The x coordinate of the hero
        self.speed (int) The speed of the hero
        return: none
        """
        self.rect.x -= self.speed
    def move_right(self):
        """
        Sets up the ability for the hero to move right
        args: self.rect.x (int) The x coordinate of the hero
        self.speed (int) The speed of the hero
        return: none
        """
        self.rect.x += self.speed

    def fight(self, opponent):
        """
        Allows the hero to fight the enemies and beat them or lose health points based on random chance
        args: self.health (int) The number of health points the hero has (left)
        return: False if the hero loses against the enemy, True if the hero wins against the enemy
        """
        if(random.randrange(3)):
            self.health -= 1
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
        return True
