import sys
import os
location = os.path.realpath('Assets')
if location not in sys.path:
    sys.path.append(location)
class room():
    directions = ['north','south','east','west']
    north = False
    south = False
    east = False
    west = False
    items = []
    hiddenItems = []
    text = ""
    invText = ""
    secondText = ""
    action = ""
    lock = False
    key = None
    roomCount = 0
    invItem = False
    options = ['none']
    def __init__(self):
        north = self.north
        south = self.south
        east = self.east
        west = self.west
        items = self.items
        text = self.text
        options = self.options
        lock = self.lock
        key = self.key
        invText = self.invText
        hiddenItems = self.hiddenItems
        secondText = self.secondText
        roomCount = self.roomCount
        invItem = self.invItem
        directions = self.directions
    def EnterRoom(self):
        if self.roomCount == 0:
            print(self.text)
        else:
            print(self.secondText)
        for i in self.options:
            print('-'+i)
    def ChangeRoom(self):
        curroom = self.name
        outval = False
        if self.action == 'north':
            if self.north:
                outval = (self.north).useDoor(curroom)
        elif self.action == 'south':
            if self.south:
                outval = (self.south).useDoor(curroom)
        elif self.action == 'east':
            if self.east:
                outval = (self.east).useDoor(curroom)
        elif self.action == 'west':
            if self.west:
                outval = (self.west).useDoor(curroom)
        return outval
    def printItems(self):
        for i in self.items:
            print('-'+i.disName)

    def pickUp(self):
        if self.action == 'Pick up':
            self.printItems()
            item = input('Which Item?')
            for i in self.items:
                if item == i.disName:
                    inventory.append(i)
                    return i

    def doAction(self):
        self.action = input("Option: ")
        return self.action
    def doOption(self):
        next = True
        if self.action in self.options:
            if self.action == 'Leave Room':
                self.action = input('Direction: ').lower()
                return self.action
            elif self.action == 'Pick up':
                item = self.pickUp()
                self.items.remove(item)
                return next
            elif self.action == 'Items in Room':
                for i in self.items:
                    print('-'+i.disName)
            elif self.action == 'Investigate':
                print(self.invText)
                if self.invItem == True:
                    for i in self.hiddenItems:
                        inventory.append(i)
                        self.hiddenItems.remove(i)
                        self.roomCount += 1
            elif self.action == 'Display Inventory':
                for i in inventory:
                    print('-'+i.disName)

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
                if self.key in inventory:
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


class item():
    disName = ''
    isKey = False
    def __init__(self):
        disName = self.disName
        isKey = self.isKey

inventory = []
dirlist = ['north', 'south', 'east', 'west']
RoomOne = room()
RoomTwo = room()
RoomThree = room()
DoorTwo = door()
DoorOne = door()
KeyOne = item()
RoomOne.name = RoomOne
RoomOne.north = DoorOne
RoomOne.text = 'This is Room One'
RoomOne.options = ['Leave Room']
KeyOne.disName = 'Key'
KeyOne.isKey = True
RoomTwo.name = RoomTwo
RoomThree.name = RoomThree
RoomTwo.items = [KeyOne]
RoomTwo.south = DoorOne
RoomTwo.west = DoorTwo
RoomThree.east = DoorTwo
DoorOne.north = RoomTwo
DoorOne.south = RoomOne
DoorTwo.west = RoomThree
DoorTwo.east = RoomTwo
DoorTwo.key = KeyOne
DoorTwo.lock = True
RoomTwo.text = 'This is Room Two'
RoomThree.text = 'This is Room Three'
RoomTwo.options  = ['Leave Room','Pick up','Display Inventory','Items in Room']
RoomThree.options = ['Leave Room']
currentroom = RoomOne
def main(currentroom):
    x = 1
    while x:
        currentroom.EnterRoom()
        currentroom.doAction()
        nextaction = currentroom.doOption()
        if nextaction in dirlist:
            nextroom = currentroom.ChangeRoom()
            if nextroom != False:
                currentroom = nextroom
            else:
                print('No Room')
        elif nextaction:
            pass
main(currentroom)