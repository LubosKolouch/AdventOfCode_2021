#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Advent of Code 2021 Day 20 """


class Day20:
    """ Day 20 AoC """

    def __init__(self, in_file: str):
        with open(in_file, "r") as my_in:
            lines = [line.strip() for line in my_in.readlines()]

        self.algo = [item == "#" for item in lines[0]]

        self.map = {}

        for x, row in enumerate(lines[2:]):
            for y, item in enumerate(row):
                if item == "#":
                    self.map[(x, y)] = '1'

        self.max_n = max(row for row, _ in self.map) + 1

    def get_bin(self, coord):
        """ Get the binary number for coord """

        new_bin = ""
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                try:
                    new_bin += str(self.map[(x + coord[0], y + coord[1])])
                except KeyError:
                    new_bin += "0"

        new_bin = int(new_bin, 2)
        return new_bin

    def process_image(self, rounds):
        """ Do the processing """

        for my_round in range(rounds):
            new_map = {}
            for x in range(-self.max_n - 1, 2 * self.max_n + 1):
                for y in range(-self.max_n - 1, 2 * self.max_n + 1):
                    new_bin = self.get_bin((x, y))
                    if self.algo[new_bin]:
                        new_map[(x, y)] = "1"

            num_count = 0
            for x in range(-2 - rounds, self.max_n + 2 + rounds):
                for y in range(-2 - rounds, self.max_n + 2 + rounds):
                    try:
                        if new_map[(x, y)] == "1":
                            num_count += 1
                    except KeyError:
                        pass

            self.map = new_map
        return num_count


def test_day_20():
    """ Run the tests """

    day20 = Day20("input20_test")
    day20.get_bin((0, 0))
    day20.process_image(rounds=2)
    assert 1 == 2


def main():
    """ Run the exercise """
    day20 = Day20("input20")
    print(day20.process_image(rounds=2))

    day20 = Day20("input20")
    print(day20.process_image(rounds=50))


if __name__ == "__main__":
    main()
