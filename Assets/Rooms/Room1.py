from Objects import *
RoomOne.name = RoomOne
RoomOne.north = DoorOne
RoomOne.text = 'The room is too dark to see clearly, there appears to be an exit to the north'
RoomOne.options = ['Leave Room']

def pRoom():
	print(RoomOne.north)
	print(RoomOne.text)