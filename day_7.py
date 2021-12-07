#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import numpy as np


class Crabs:
    """ Play with the crabs """
    def __init__(self, input_file: str):
        self.in_list = np.genfromtxt(input_file, delimiter=",", dtype=int)

    @property
    def get_part1(self):
        """ Find part1 """
        min_dist = 999999999
        for i in range(min(self.in_list), max(self.in_list) + 1):
            distance = 0
            for j in self.in_list:
                distance += abs(j - i)
            if distance < min_dist:
                min_dist = distance

        return min_dist

    @property
    def get_part2(self):
        """ Find part2 """

        min_dist = 999999999
        for i in range(min(self.in_list), max(self.in_list) + 1):
            distance = 0
            fuel = 0
            for j in self.in_list:
                distance = abs(j - i)
                fuel += sum(range(1, distance + 1))
            if fuel < min_dist:
                min_dist = fuel

        return min_dist


def test_day_1():
    """ Test the solution for day 1 """

    crabs = Crabs("input7_test")
    assert crabs.get_part1 == 37
    assert crabs.get_part2 == 168


def main():
    """ Go! """
    crabs = Crabs("input7")
    print(crabs.get_part1)
    print(crabs.get_part2)


if __name__ == "__main__":
    main()
