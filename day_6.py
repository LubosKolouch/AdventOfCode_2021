#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from collections import Counter
import numpy as np


class LanternPopulation:
    """ AoC Day 6"""
    def __init__(self):
        self.init_list = None

    def load_list(self, name: str):
        """ Load the input """
        self.init_list = np.genfromtxt(name, delimiter=",", dtype="int")

    def get_result(self, rounds: int):
        """ Count the population """

        day = 0
        population = Counter(self.init_list)

        while day < rounds:
            new_dict = defaultdict(int)

            # shift the rest
            for i in range(1, 9):
                new_dict[i - 1] = population[i]
            # 0 => 8
            new_dict[8] = population[0]

            # 0 => 6
            new_dict[6] += population[0]

            population = new_dict.copy()

            day += 1

        return sum(population.values())


def test_day_6():
    """ Run the tests"""

    lantern = LanternPopulation()
    lantern.load_list("input6_test")

    assert lantern.get_result(18) == 26


def main():
    """ Go! """

    lantern = LanternPopulation()
    lantern.load_list("input6")

    print(f"Part1: {lantern.get_result(80)}")
    print(f"Part2: {lantern.get_result(256)}")


if __name__ == "__main__":
    main()
