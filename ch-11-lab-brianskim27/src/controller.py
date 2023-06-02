import sys
import pygame
import random
from src import hero
from src import enemy


class Controller:
    def __init__(self, width=640, height=480):
        """
        Initializes and sets up the game
        args: self.width (int) Width (left to right) of the screen
        self.height (int) Height (top to bottom) of the screen
        self.screen (display) The screen that is displayed
        self.background (surface) Background of the screen
        self.enemies (sprite) Group of enemies as sprites
        num_enemies (int) The number of enemies in the game
        x (int) Random x coordinate for each enemy
        y (int) Random y coordinate for each enemy
        self.hero (class)
        self.all_sprites (sprite) All the sprites, including the hero and the enemies
        self.state (str) String labeled "GAME"
        return: none
        """
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((250, 250, 250))  # set the background to white
        pygame.font.init()  # you have to call this at the start, if you want to use this module.
        pygame.key.set_repeat(1, 50)  # initialize a held keey to act as repeated key strikes
        """Load the sprites that we need"""

        self.enemies = pygame.sprite.Group()
        num_enemies = 3
        for i in range(num_enemies):
            x = random.randrange(100, 400)
            y = random.randrange(100, 400)
            self.enemies.add(enemy.Enemy("Boogie", x, y, 'assets/enemy.png'))
        self.hero = hero.Hero("Conan", 50, 80, "assets/hero.png")
        self.all_sprites = pygame.sprite.Group((self.hero,) + tuple(self.enemies))
        self.state = "GAME"

    def mainLoop(self):
        """
        Controls the state of the game
        args: self.state (str) String labeled as either "GAME" or "GAMEOVER"
        return: none
        """
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        """
        Enables the hero to move based on key inputs from the user
        args: self.state (str) String labeled as "GAME"
        event.type (text) The input of the event that is taking place
        event.key (int) The key that is inputted on the keyboard from the user
        fights (list) The hero and the enemies colliding as means of fighting
        e (int) The enemy that the fighter is fighting
        self.hero.health (int) The number of health points the hero has
        self.state (str) String labeled as "GAMEOVER"
        return: none
        """
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move_right()

            # check for collisions
            fights = pygame.sprite.spritecollide(self.hero, self.enemies, True)
            if(fights):
                for e in fights:
                    if(self.hero.fight(e)):
                        e.kill()
                        self.background.fill((250, 250, 250))
                    else:
                        self.background.fill((250, 0, 0))
                        self.enemies.add(e)

            # redraw the entire screen
            self.enemies.update()
            self.screen.blit(self.background, (0, 0))
            if(self.hero.health == 0):
                self.state = "GAMEOVER"
            self.all_sprites.draw(self.screen)

            # update the screen
            pygame.display.flip()

    def gameOver(self):
        """
        Ends the game and shows a gameover screen
        args: myfont (font) Changes the system font
        message (str) Writes out 'Game Over'
        event.type (text) The input of the event taking place
        return: none
        """
        self.hero.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
