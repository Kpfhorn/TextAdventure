import Objects
import copy

class saveState():
    saveObject = ''
    LastState = ''

    def saveObj(self):
        self.LastState = copy.deepcopy(self.saveObject)

sRoomOne = saveState()
sRoomTwo = saveState()
sRoomThree = saveState()
sRoomFour = saveState()
sDoorOne = saveState()
sDoorTwo = saveState()
sDoorThree = saveState()
sKeyOne = saveState()
sP1 = saveState()
saveStates = [sRoomOne, sRoomTwo,sRoomThree, sRoomFour, sDoorOne, sDoorTwo, sDoorThree, sKeyOne, sP1]


def makeSaves():
    for obj in saveStates:
        obj.saveObject = Objects.SaveList[saveStates.index(obj)]


def save():
    for obj in saveStates:
        obj.saveObj()
    print('Game Saved!')

def load():
    for obj in saveStates:
        Objects.SaveList[saveStates.index(obj)] = copy.deepcopy(obj.LastState)
    for obj in Objects.SaveList:
        if obj.isCurrent:
            outval = obj
            return outval



