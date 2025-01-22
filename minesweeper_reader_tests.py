import os
import unittest
from dataclasses import field

from minesweeper_reader import *

class MinesweeperTest(unittest.TestCase):

    def test_zero_case(self):
        sample_input = [
                        '',
        ]

        sample_output = '\n'

        play = MineSweeperGenerator(field=sample_input)
        output = play.display()

        self.assertEqual(output, sample_output)


    def test_all_mine_case(self):
        sample_input = [
                        '***',
                        '***',
                        '***',
        ]

        sample_output = \
            '\n***' \
            '\n***' \
            '\n***' \

        play = MineSweeperGenerator(field=sample_input)
        output = play.display()

        self.assertEqual(output, sample_output)


    def test_no_mine_case(self):
        sample_input = [
                        '...',
                        '...',
                        '...',
        ]

        sample_output = \
            '\n000' \
            '\n000' \
            '\n000' \

        play = MineSweeperGenerator(field=sample_input)
        output = play.display()

        self.assertEqual(output, sample_output)


    def test_8_mine_case(self):
        sample_input = [
                        '***',
                        '*.*.',
                        '***',
        ]

        sample_output = \
            '\n***' \
            '\n*8*' \
            '\n***' \

        play = MineSweeperGenerator(field=sample_input)
        output = play.display()

        self.assertEqual(output, sample_output)


    def test_edge_mine_case(self):
        sample_input = [
                        '*..',
                        '...',
                        '..*',
        ]

        sample_output = \
            '\n*10' \
            '\n121' \
            '\n01*' \

        play = MineSweeperGenerator(field=sample_input)
        output = play.display()

        self.assertEqual(output, sample_output)


    def test_center_mine_case(self):
        sample_input = [
                        '...',
                        '.*.',
                        '...',
        ]

        sample_output = \
            '\n111' \
            '\n1*1' \
            '\n111' \

        play = MineSweeperGenerator(field=sample_input)
        output = play.display()

        self.assertEqual(output, sample_output)

    def test_generic_case(self):
        sample_input = [
                        '.....',
                        '*....',
                        '*...*',
                        '....*',
                        '..*..',
        ]

        sample_output = \
             '\n11000\n'\
             '*2011\n'\
             '*202*\n'\
             '1213*\n'\
             '01*21'\

        play = MineSweeperGenerator(field=sample_input)
        output = play.display()

        self.assertEqual(output, sample_output)


    def test_multiple_stress_cases(self):
        """used generate_minefield_input to make random fields, made a control file and now assessing against that"""
        play = MineSweeperFactory(input_file='minefields.txt', output_file='minefields_output_test.txt')
        play.display_all()

        with open('minefields_output_test.txt', 'r') as f:
            output = f.readlines()
        with open('minefields_output_control.txt', 'r') as f:
            control = f.readlines()

        self.maxDiff = None
        self.assertEqual(control, output)
