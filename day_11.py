#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Advent of Code 2021 Day 11 """

import numpy as np


class Flash:
    """ Day 11 AoC """
    def __init__(self, in_file: str):
        self.map = np.genfromtxt(in_file, delimiter=1, dtype=int)
        self.x_max = len(self.map)
        self.y_max = len(self.map[0])
        self._flashed = {}
        self._flash_count = 0
        self.part1 = 0
        self.part2 = 0

    def count_flashes(self, rounds: int):
        """ Part 1 """

        my_round = 0

        while 1:
            my_round += 1
            self.map += 1
            self._flashed = {}

            seen_flash = 1

            while seen_flash:
                seen_flash = 0
                flashed_items = np.where(self.map > 9)
                for item in zip(flashed_items[0], flashed_items[1]):
                    seen_flash = 0 or self.flash_item(item)

            for pos in self._flashed:
                self.map[pos] = 0

            if len(self._flashed.keys()) == self.x_max * self.y_max:
                self.part2 = my_round

            if my_round == rounds:
                self.part1 = self._flash_count

            if self.part2:
                break

    def flash_item(self, item):
        """ Flash the point """

        if self._flashed.get(item, 0) == 1:
            return 0

        self._flashed[item] = 1

        self.map[max(0, item[0] - 1):min(self.x_max, item[0] + 2),
                 max(0, item[1] - 1):min(self.y_max, item[1] + 2)] += 1

        self.map[item] = 0

        self._flash_count += 1
        return 1


def test_day_11():
    """ Run the tests """

    submarine = Flash("input11_test")
    submarine.count_flashes(rounds=100)
    assert submarine.part1 == 1656
    assert submarine.part2 == 195


def main():
    """ Run the exercise """
    submarine = Flash("input11")
    submarine.count_flashes(rounds=100)
    print(submarine.part1)
    print(submarine.part2)


if __name__ == "__main__":
    main()
