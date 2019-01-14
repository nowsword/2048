def judgeEnd(map, end=2048):
    empty = False
    for row in map:
        for i in row:
            if i == end:
                return 2
            if i == None:
                empty = True
    if empty:
        return 0
    lx = len(map)
    if lx == 0:
        return 1
    ly = len(map[0])
    for x in range(lx):
        for y in range(ly):
            if x != lx - 1 and map[x][y] == map[x + 1][y]:
                return 0
            if y != ly - 1 and map[x][y] == map[x][y + 1]:
                return 0
    return 1
