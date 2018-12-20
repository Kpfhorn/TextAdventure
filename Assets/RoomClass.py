import Objects
import SaveClass


class room():
    isCurrent = False
    directions = ['north', 'south', 'east', 'west']
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
    checkpoint = False
    options = ['none']
    constants = ['I', 'Leave Room', 'Save', 'C']

    def EnterRoom(self):
        if self.roomCount == 0:
            print(self.text)
        else:
            print(self.secondText)
        for i in self.options:
            print('-'+i)

    def ChangeRoom(self):
        curroom = self.name
        self.isCurrent = False
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
        if self.action == 'Pick Up':
            self.printItems()
            try:
                item = input('Which Item?')
                for i in self.items:
                    if item == i.disName:
                        Objects.P1.inventory.append(i)
                        return i
            except:
                pass

    def doAction(self):
        self.action = input("Option: ")
        return self.action

    def doOption(self):
        if self.action in self.options or self.constants:
            if self.action == 'Leave Room':
                self.action = input('Direction: ').lower()
                return self.action
#            elif self.action == 'Investigate':
#                print(self.invText)
#                if self.invItem == True:
#                    for i in self.hiddenItems:
#                        P1.inventory.append(i)
#                        self.hiddenItems.remove(i)
#                        self.roomCount += 1
            elif self.action == 'I':
                for i in Objects.P1.inventory:
                    print('-'+i.disName)
            elif self.action == 'Save':
                if self.checkpoint == True:
                    SaveClass.save()
            elif self.action == 'C':
                print('Player Health:',Objects.P1.health)
                print('Lives:', Objects.P1.lives)


class roomOne(room):
    def roomAction(self):
        outval = self.doOption()
        if outval:
            return outval


class roomTwo(room):
    def roomAction(self):
        outval = self.doOption()
        if self.action == 'Pick Up':
            item = self.pickUp()
            self.items.remove(item)
            outval = True
            return outval
        elif self.action == 'Items in Room':
                    for i in self.items:
                        print('-'+i.disName)
        if outval:
            return outval


class roomThree(room):
    def roomAction(self):
        outval = self.doOption()
        Objects.P1.health -= 10
        if outval:
            return outval


class roomFour(room):
    def roomAction(self):
        outval = self.doOption()
        if outval:
            return outval
