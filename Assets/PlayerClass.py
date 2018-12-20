from Objects import *
from SaveClass import *

class player():
    health = 100
    lives = 3
    inventory = []
    save = ''

    def checkhealth(self):
        outval = True
        while self.lives:
            if self.health == 0:
                outval = False
                return outval
            else:
                return outval



