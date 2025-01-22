
import random
from idlelib.editor import keynames

import numpy as np


class MineSweeperGenerator:
    def __init__(self, field=[]):
        """Minesweeper generator, needs a list of strings to create the numbered version"""
        # give it something so it doesn't bonk out
        if len(field) == 0:
            field = [[]]

        self.height = len(field)
        self.width = len(field[0])
        self.nodes = {}

        # build grid dictionary
        for x in range(self.height):
            self.nodes[x] = {}
            for y in range(self.width):
                self.nodes[x][y] = field[x][y]

        self.generate()


    def generate(self):
        """generates numbered grid points using dict"""
        for h in range(self.height):
            for w in range(self.width):
                # if "." replace with 0
                if self.nodes[h][w] == '.':
                    self.nodes[h][w] = 0

                # else if * then add 1 to all around
                elif self.nodes[h][w] == '*':
                    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:

                        try:
                            if self.nodes[h+i][w+j]=='*':
                                continue
                            else:
                                self.nodes[h+i][w+j] += 1
                        # if type error, means I haven't initalized data yet,
                        except TypeError:
                            self.nodes[h+i][w+j] = 1
                        # key error means out of index/not found for dict
                        except KeyError:
                            pass


    def display(self):
        """Displays minefield with numbers associated to adjacent mines"""
        out_string = ''
        for h in range(self.height):
            out_string+='\n'
            for w in range(self.width):
                out_string+=str(self.nodes[h][w])
        return out_string


class MineSweeperFactory:
    def __init__(self, input_file='minesweeper_input_TC.txt', output_file='minesweeper_output.txt'):
        """Generic factory class to store several minesweeper fields"""
        with open(input_file, 'r') as f:
            self.input_lines = f.readlines()

        self.output_file = output_file
        self.input_file = input_file
        self.fields = {}
        self.field_obj = {}
        self.build_fields()


    def build_fields(self):
        """builds all the minefields using dict to store them"""
        i=0
        for line in self.input_lines:
            # if empty lines
            if not line.split():
                continue

            elif line.split()[0][0]!='.' and line.split()[0][0]!='*':
                i+=1
                self.fields[i] = []

            else:
                self.fields[i].append(line.strip())

        for field in self.fields:
            self.field_obj[field] = MineSweeperGenerator(self.fields[field])
            # check width, if 0 just get rid of it
            if self.field_obj[field].width == 0:
                self.field_obj.pop(field)

    def display_all(self):
        """displays/writes all the minefields"""
        output = ''
        i=0
        for field in self.field_obj.values():
            i+=1
            output+=f'Field #{i}: {field.display()}\n\n'

        with open(self.output_file, 'w') as f:
            f.write(output)



# if __name__ == '__main__':
#     play = MineSweeperFactory('minefields.txt', 'minesweeper_output.txt')
#     play.display_all()



