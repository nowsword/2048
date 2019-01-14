def _printLine(width, body='_', side=' ', sep='|'):
    print(side + (body * 6 + sep) * (width - 1) + body * 6 + side)


def _printNumber(num, isTarget):
    print('|', end='')
    mark = '>' if isTarget else ' '
    if num == None:
        print(' ' * 6, end='')
    elif num < 10:
        print(mark + '  %d  ' % num, end='')
    elif num < 100:
        print(mark + ' %d  ' % num, end='')
    elif num < 1000:
        print(mark + ' %d ' % num, end='')
    else:
        print(mark + '%d ' % num, end='')


def printMap(map, target=None):
    lx = len(map)
    if lx == 0:
        return
    ly = len(map[0])
    _printLine(ly, '_', ' ', '_')
    for x in range(lx):
        _printLine(ly, ' ', '|')
        for y in range(ly):
            _printNumber(map[x][y], target and x ==
                         target[0] and y == target[1])
        print('|')
        _printLine(ly, '_', '|')
