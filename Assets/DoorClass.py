from PlayerClass import *
import Objects


class door():
    lock = False
    north = False
    south = False
    east = False
    west = False
    password = False
    key = False
    passtext = False
    def __init__(self):
        lock = self.lock
        north = self.north
        south = self.south
        east = self.east
        west = self.west
        password = self.password
        key = self.key
        passtext = self.passtext
    def useDoor(self, currentroom):
        nextroom = ''
        if currentroom == self.north:
            nextroom = self.south
        elif currentroom == self.south:
            nextroom = self.north
        elif currentroom == self.east:
            nextroom = self.west
        elif currentroom == self.west:
            nextroom = self.east
        if self.lock == False:
            return nextroom
        elif self.lock:
            if self.key:
                if self.key in Objects.P1.inventory:
                    print('Door unlocked!')
                    self.lock = False
                    return nextroom
                else:
                    print('You need a key to open this door')
                    return currentroom
            elif self.password:
                print(self.passtext)
                pass_try = input('Password? ')
                if pass_try == self.password:
                    print('door unlocked!')
                    self.lock = False
                    return nextroom
                else:
                    print('Wrong Password!')