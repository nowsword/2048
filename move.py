def _move(queue):
    l = len(queue)
    if l < 2:
        return queue, 0
    q = []
    flag = False
    sum = 0
    for i in queue:
        if i != None:
            if flag and i == q[-1]:
                q[-1] *= 2
                flag = False
                sum += q[-1]
            else:
                q.append(i)
                flag = True
    q += [None] * (l - len(q))
    return q, sum


def moveUp(map):
    lx = len(map)
    if lx == 0:
        return False, 0
    ly = len(map[0])
    flag = False
    sum = 0
    for y in range(ly):
        queue = []
        for x in range(lx):
            queue.append(map[x][y])
        res = _move(queue)
        sum += res[1]
        for x in range(lx):
            if map[x][y] != res[0][x]:
                map[x][y] = res[0][x]
                flag = True
    return flag, sum


def moveDown(map):
    lx = len(map)
    if lx == 0:
        return False, 0
    ly = len(map[0])
    flag = False
    sum = 0
    for y in range(ly):
        queue = []
        for x in reversed(range(lx)):
            queue.append(map[x][y])
        res = _move(queue)
        sum += res[1]
        for x in range(lx):
            if map[x][y] != res[0][lx - x - 1]:
                map[x][y] = res[0][lx - x - 1]
                flag = True
    return flag, sum


def moveLeft(map):
    lx = len(map)
    if lx == 0:
        return False, 0
    ly = len(map[0])
    flag = False
    sum = 0
    for x in range(lx):
        queue = []
        for y in range(ly):
            queue.append(map[x][y])
        res = _move(queue)
        sum += res[1]
        for y in range(ly):
            if map[x][y] != res[0][y]:
                map[x][y] = res[0][y]
                flag = True
    return flag, sum


def moveRight(map):
    lx = len(map)
    if lx == 0:
        return False, 0
    ly = len(map[0])
    flag = False
    sum = 0
    for x in range(lx):
        queue = []
        for y in reversed(range(ly)):
            queue.append(map[x][y])
        res = _move(queue)
        sum += res[1]
        for y in range(ly):
            if map[x][y] != res[0][ly - y - 1]:
                map[x][y] = res[0][ly - y - 1]
                flag = True
    return flag, sum
