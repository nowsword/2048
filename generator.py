import random
import math


def generate(map):
    lx = len(map)
    if lx == 0:
        return map
    ly = len(map[0])
    q = []
    for x in range(lx):
        for y in range(ly):
            if map[x][y] == None:
                q.append((x, y))
    pos = q[math.floor(random.random() * len(q))]
    value = math.ceil(random.random() * 2) * 2
    map[pos[0]][pos[1]] = value
    return pos


def newMap(width, height):
    num = width * height
    a = math.floor(random.random() * num)
    b = math.floor(random.random() * (num - 1))
    if b >= a:
        b += 1
    posA = (a // width, a % height)
    posB = (b // width, b % height)
    valueA = math.ceil(random.random() * 2) * 2
    valueB = math.ceil(random.random() * 2) * 2
    map = [[None] * width for i in range(height)]
    map[posA[0]][posA[1]] = valueA
    map[posB[0]][posB[1]] = valueB
    return map
