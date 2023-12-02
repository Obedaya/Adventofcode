import fileinput
import math as m


def calculateDistance(x1, x2, y1, y2):
    return m.sqrt((x1-x2)**2+(y1-y2)**2)


def calculateMax(x1, x2, y1, y2):
    if abs(x2-x1) > abs(y2-y1):
        if abs(x2-x1) > 0 and abs(y2-y1) > 0:
            return 2
        else:
            return 0
    else:
        if abs(x2 - x1) > 0 and abs(y2 - y1) > 0:
            return 2
        else:
            return 1


def sign(x):
    return 1 if x > 0 else(-1 if x < 0 else 0)


def moveHead():
    if line[0] == "U":
        coordH[1] += int(str(line[2:-1]))
    elif line[0] == "D":
        coordH[1] -= int(str(line[2:-1]))
    elif line[0] == "L":
        coordH[0] -= int(str(line[2:-1]))
    elif line[0] == "R":
        coordH[0] += int(str(line[2:-1]))


def moveTail():
    while calculateDistance(coordH[0], coordT[0], coordH[1], coordT[1]) > m.sqrt(2):
        i = calculateMax(coordH[0], coordT[0], coordH[1], coordT[1])
        if i == 2:
            coordT[0] += sign(coordH[0]-coordT[0])
            coordT[1] += sign(coordH[1] - coordT[1])
        else:
            coordT[i] += sign(coordH[i]-coordT[i])
        coord = str(coordT[0]) + "|" + str(coordT[1])
        visited.add(coord)

    print("Coordinate Head: ", coordH)
    print("Coordinate Tail: ", coordT)

suppengemuese
coordH = [0, 0]
coordT = [0, 0]
visited = {"0|0"}
for line in fileinput.input(files='input9.txt'):
    moveHead()
    moveTail()

print(len(visited))