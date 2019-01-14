import generator
import judgeEnd
import move
import printMap
import msvcrt


class game:
    def __init__(self, end=2048, width=4, height=4):
        self.width = width
        self.height = height
        self.end = end
        self.status = 0
        self.map = generator.newMap(width, height)
        self.stepCount = 0
        self.score = 0
        print('_____________________________\n\nNew Game  步数：0  分数：0')
        printMap.printMap(self.map)

    def __print(self, gene=None):
        print('\n步数：' + str(self.stepCount) + '  分数：' + str(self.score))
        printMap.printMap(self.map, gene)

    def __afterMove(self):
        self.__print(generator.generate(self.map))
        self.status = judgeEnd.judgeEnd(self.map, self.end)
        if self.status == 2:
            print('\nWin!\n_____________________________')
        elif self.status == 1:
            print('\nGame Over!\n_____________________________')

    def moveUp(self):
        if self.status == 0:
            res = move.moveUp(self.map)
            if res[0]:
                self.stepCount += 1
                self.score += res[1]
                self.__afterMove()

    def moveDown(self):
        if self.status == 0:
            res = move.moveDown(self.map)
            if res[0]:
                self.stepCount += 1
                self.score += res[1]
                self.__afterMove()

    def moveLeft(self):
        if self.status == 0:
            res = move.moveLeft(self.map)
            if res[0]:
                self.stepCount += 1
                self.score += res[1]
                self.__afterMove()

    def moveRight(self):
        if self.status == 0:
            res = move.moveRight(self.map)
            if res[0]:
                self.stepCount += 1
                self.score += res[1]
                self.__afterMove()


a = game()
while True:
    try:
        ch = msvcrt.getch().decode().upper()
        if ch == 'Q':
            exit()
        elif ch == 'N':
            a = game()
        elif ch == 'W':
            a.moveUp()
        elif ch == 'S':
            a.moveDown()
        elif ch == 'A':
            a.moveLeft()
        elif ch == 'D':
            a.moveRight()
    except UnicodeDecodeError:
        pass
