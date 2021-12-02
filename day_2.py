#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Advent Of Code 2021 Day 2"""


class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        self.methods = {}
        self._init_methods()

    def _init_methods(self):
        """ Prepare methods for each move """
        self.methods['forward'] = self.forward
        self.methods['up'] = self.up
        self.methods['down'] = self.down
        self.methods['forward_aim'] = self.forward_aim
        self.methods['up_aim'] = self.up_aim
        self.methods['down_aim'] = self.down_aim

    def forward(self, step: int):
        """ Move the sub forward """
        self.horizontal += step

    def forward_aim(self, step: int):
        """ Move the sub forward """
        self.horizontal += step
        self.depth += self.aim * step

    def up(self, step: int):
        """ Move the sub up """
        self.depth -= step

    def up_aim(self, step: int):
        """ Move the sub up """
        self.aim -= step

    def down(self, step: int):
        """ Move the sub down """
        self.depth += step

    def down_aim(self, step: int):
        """ Move the sub down """
        self.aim += step

    @property
    def get_result(self):
        """ Return the solution for Part1 and Part2 """
        return self.depth * self.horizontal


def main():
    """ Do the daily tasks """
    with open("input2", "r") as in_file:
        instructions = in_file.read().split("\n")

    submarine_1 = Submarine()

    for instr in instructions:
        if instr:
            move, step = instr.split(' ')
            submarine_1.methods[move](int(step))

    print(submarine_1.get_result)

    submarine_2 = Submarine()

    for instr in instructions:
        if instr:
            move, step = instr.split(' ')
            submarine_2.methods[move + "_aim"](int(step))

    print(submarine_2.get_result)


if __name__ == "__main__":
    main()
