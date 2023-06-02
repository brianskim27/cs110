# CS 110
## Chapter 11 - Lab - Working with Pygame


### [Assignment Description](https://docs.google.com/document/d/1kFLQs7Lepb8hcYOrZq5scmRmdcNkIwWZ6Kb85_0bCVY/edit?usp=sharing)

***
Replace anything surrounded by the `< >` symbols._

## SUMMARY:
In Part A, I changed the update function in enemy.py to have the enemies move (using x and y coordinates) by a random value of -1, 0, or 1. In Part B, I created boundaries for the screen that stops the enemies from leaving it as it moves a random distance.
#### Unique Feature
I created boundaries for the screen that stops the enemies from leaving it as it moves a random distance. I first created a variable that stores the size of the sprite image. Then, I used if statements to stop the enemies from moving past the boundaries of the screen, which I made by using the height and width of the screen. Lastly, I kept Part A as an else statement to continuously let the enemies move a random distance within the screen.

## GRACE DAYS
Grace days used for this assignment: 0

Grace days remaining: 5/5

## KNOWN BUGS AND INCOMPLETE PARTS:
There was a bug where self.rect.y -= 1 would still let the enemies go past the bottom of the screen, but self.rect.y += -1 would allow the code to function properly. Aren't self.rect.y -= 1 and self.rect.y += -1 the same thing?

## REFERENCES:
N/A

## MISCELLANEOUS COMMENTS:
N/A
