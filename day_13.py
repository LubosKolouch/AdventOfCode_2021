#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Advent of Code 2021 Day 13 """

import re


class Folding:
    """ Day 13 AoC """
    def __init__(self, in_file: str):
        with open(in_file, "r") as file:
            data, self.folding = [
                part.splitlines() for part in file.read().split('\n\n')
            ]

        self.grid = {}

        self.max_x = 0
        self.max_y = 0
        for item in data:
            y, x = list(map(int, item.split(",")))
            self.grid[x, y] = "█"
            if x > self.max_x:
                self.max_x = x

            if y > self.max_y:
                self.max_y = y

    def print_grid(self):
        """ Print the grid """

        for x in range(self.max_x):
            for y in range(self.max_y):
                if self.grid.get((x, y)):
                    print("█", end="")
                else:
                    print(" ", end="")

            print("")

    def fold(self, part: int):
        """ Do the folds """

        for next_fold in self.folding:
            axis, count = re.findall(r'(.)=(\d+)', next_fold)[0]
            count = int(count)

            for item in dict(self.grid):

                if axis == "y" and item[0] > count:
                    item_x, item_y = item
                    self.grid[item_x - 2 * (item_x - count), item_y] = "#"
                    del self.grid[item]

                if axis == "x" and item[1] > count:
                    item_x, item_y = item
                    self.grid[item_x, item_y - 2 * (item_y - count)] = "#"
                    del self.grid[item]

            if axis == "y":
                self.max_x = count

            if axis == "x":
                self.max_y = count

            if part == 1:
                return len(self.grid)
        self.print_grid()

        return len(self.grid)


def test_day_13():
    """ Run the tests """

    folding = Folding("input13_test")
    assert folding.fold(part=1) == 17
    assert folding.fold(part=2) == 16


def main():
    """ Run the exercise """
    folding = Folding("input13")
    print(folding.fold(part=1))

    folding.fold(part=2)


if __name__ == "__main__":
    main()
