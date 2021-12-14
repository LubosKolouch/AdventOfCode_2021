#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Advent of Code 2021 Day 14 """

import re
from collections import Counter, defaultdict


class Polymer:
    """ Day 14 AoC """
    def __init__(self, in_file: str):
        with open(in_file, "r") as file:
            init_polymer, self.ruleset = [
                part.splitlines() for part in file.read().split('\n\n')
            ]

        self.rules = {}

        for item in self.ruleset:
            fr, to = item.split(" -> ")
            self.rules[fr] = to

        self.polymer_chars = defaultdict(int)
        self.two_chars = defaultdict(int)

        for pos, char in enumerate(init_polymer[0][:-1]):
            self.polymer_chars[char] += 1
            two_char = char + init_polymer[0][pos + 1]
            if self.rules.get(two_char, 0):
                self.two_chars[two_char] += 1

        self.polymer_chars[init_polymer[0][-1]] = 1

    def create_polymer(self, rounds: int):
        """ Fold the polymer as needed """
        for my_round in range(rounds):

            orig_two_chars = self.two_chars.copy()
            for item, count in orig_two_chars.items():

                if count == 0:
                    continue

                self.two_chars[item] -= count

                if self.rules.get(item, 0):
                    new_char = self.rules[item]

                    self.polymer_chars[new_char] += count

                    self.two_chars[item[0] + new_char] += count
                    self.two_chars[new_char + item[1]] += count

        counts = sorted(self.polymer_chars.values())
        return counts[-1] - counts[0]


def test_day_14():
    """ Run the tests """

    polymer = Polymer("input14_test")
    assert polymer.create_polymer(10) == 1588
    polymer = Polymer("input14_test")

    assert polymer.create_polymer(40) == 2188189693529


def main():
    """ Run the exercise """
    polymer = Polymer("input14")
    print(polymer.create_polymer(rounds=10))

    polymer = Polymer("input14")
    print(polymer.create_polymer(rounds=40))


if __name__ == "__main__":
    main()
