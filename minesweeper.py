
import random

import numpy as np


class MineSweeperGenerator:
    class MineNode:
        def __init__(self, contains_mine=False):
            self.mine = contains_mine


    def __init__(self, height=None, width=None):
        if height is None:
            height = random.randint(3, 7)
        if width is None:
            width = random.randint(3, 7)

        self.height = height
        self.width = width
        self.nodes = {}

        for x in range(height):
            self.nodes[x] = {}
            for y in range(width):
                self.nodes[x][y] = 0

        self.generate()
        # self.display()

    def generate(self):
        for h in range(self.height):
            for w in range(self.width):
                # 15 ish% chance of mine
                mine = self.MineNode(random.choices([True, False], [0.15, 0.85])[0])
                if mine.mine:
                    self.nodes[h][w] = '*'
                    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                        try:
                            self.nodes[h+i][w+j] += 1
                        # if type error, means I haven't initalized data yet,
                        except (KeyError, TypeError):
                            pass


    def display(self):
        for h in range(self.height):
            print('')
            for w in range(self.width):
                print(self.nodes[h][w], end='')


class MineSweeperFactory:
    def __init__(self, list_of_fields=None):
        if list_of_fields is None:
            list_of_fields = [[]]
        self.list_of_fields = list_of_fields
        self.mine_fields = []

        for field in self.list_of_fields:
            self.mine_fields.append(MineSweeperGenerator(height=field[0], width=field[1]))


    def display_all(self):
        i=0
        for field in self.mine_fields:
            i+=1
            print('\n\nMine Field #%i:' % i, end='')
            field.display()




if __name__ == '__main__':
    fields = [
        [3, 3],
        [5, 5],
        [5, 9],
        [15, 15],
        [25, 25],
        # [100, 100]
    ]
    play = MineSweeperFactory(fields)
    play.display_all()





