#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from collections import Counter
import numpy as np


class Segments:
    """ Decode the segments """
    def __init__(self, input_file: str):
        with open(input_file, "r") as in_file:
            self.all_lines = [line.rstrip('\n') for line in in_file]

        self.letters = {}
        self.letters['abcefg'] = 0
        self.letters['cf'] = 1
        self.letters['acdeg'] = 2
        self.letters['acdfg'] = 3
        self.letters['bcdf'] = 4
        self.letters['abdfg'] = 5
        self.letters['abdefg'] = 6
        self.letters['acf'] = 7
        self.letters['abcdefg'] = 8
        self.letters['abcdfg'] = 9

    @property
    def get_part2(self):
        """ Solution part  2 """

        solution = 0
        for seg in self.all_lines:

            mapping = {}
            inputs = seg.split("|")[0].split()
            outputs = seg.split("|")[1].split()

            all_inputs = ''.join(inputs)

            lengths = defaultdict(list)

            for item in inputs:
                lengths[len(item)].append("".join(sorted(item)))

            orig_counter = Counter(all_inputs)

            items_counter = {}
            for item, value in orig_counter.items():
                items_counter[value] = item

            # f
            mapping['f'] = items_counter[9]

            # c
            for item in lengths[2][0]:
                if orig_counter[item] == 8:
                    mapping['c'] = item
                    break

            # a
            for item in lengths[3][0]:
                if item not in mapping.values():
                    mapping['a'] = item
                    break

            # b
            for item in lengths[4][0]:
                if item not in mapping.values() and orig_counter[item] == 6:
                    mapping['b'] = item
                    break

            # d
            for item in lengths[4][0]:
                if item not in mapping.values():
                    mapping['d'] = item
                    break

            # g, e
            new_items = defaultdict(int)
            for item in lengths[5]:
                for char in item:
                    if char not in mapping.values():
                        new_items[char] += 1

            for item, count in new_items.items():
                if count == 3:
                    mapping['g'] = item
                else:
                    mapping['e'] = item

            rev_mapping = {}
            for item, value in mapping.items():
                rev_mapping[value] = item

            result_num = ""
            for item in outputs:
                decoded_output = ""
                for char in "".join(sorted(item)):
                    decoded_output += rev_mapping[char]
                result_num += str(self.letters["".join(
                    sorted(decoded_output))])
            solution += int(result_num)
        return solution

    @property
    def get_part1(self):
        """ Get the solution for part1"""
        result = 0
        for seg in self.all_lines:
            parts = seg.split("|")[1].split()
            for part in parts:
                if len(part) in [2, 3, 4, 7]:
                    result += 1
        return result


def test_part_1():
    """ Test the solution for day 1 """
    segments = Segments("input8_test")

    assert segments.get_part1 == 26
    assert segments.get_part2 == 61229


def main():
    """ Go! """
    segments = Segments("input8")
    print(f"Part1 : {segments.get_part1}")
    print(f"Part2:  {segments.get_part2}")


if __name__ == "__main__":
    main()
