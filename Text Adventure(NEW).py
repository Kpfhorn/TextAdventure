import sys
from os.path import realpath
l = [realpath('Assets'), realpath('Assets\Rooms'), realpath('Assets\Doors'), realpath('Assets\Items')]
for location in l:
    if location not in sys.path:
        sys.path.append(location)
y = 1
while y:
    dirlist = ['north', 'south', 'east', 'west']
    from Everything import *

    P1.inventory = []
    SaveClass.makeSaves()
    currentroom = RoomOne
    def main(currentroom):
        print('Welcome!')
        print('Input "I" to show your inventory, and "C" to display stats')
        print('The options "Leave Room" and "I" are always available')
        x = 1
        while x:
            currentroom.isCurrent = True
            currentroom.EnterRoom()
            check = P1.checkhealth()
            if check == False:
                print('You Died! Loading Checkpoint...')
                P1.health = 100
                x -= 1
                P1.lives = x
                currentroom = SaveClass.load()
                continue
            currentroom.doAction()
            nextaction = currentroom.roomAction()
            if nextaction in dirlist:
                nextroom = currentroom.ChangeRoom()
                if nextroom != False:
                    currentroom = nextroom
                else:
                    print('No Room')
            elif nextaction:
                pass
    main(currentroom)
    print('Game Over!')
    n = input('Would you like to play again? (Y/N)')
    if n == 'Y':
        continue
    elif n== 'N':
        break