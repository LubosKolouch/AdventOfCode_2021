#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Advent of Code 2021 Day 18 """

import re
from math import ceil, floor
from itertools import permutations


class AoC18:
    """ Day 18 AoC """
    def __init__(self, in_file: str):
        with open(in_file, "r") as my_in:
            lines = [line.strip() for line in my_in.readlines()]

        self.num = ""
        self.lines = lines

    def explode(self, pos: int):
        """ Explode if possible """
        for two_digits in re.finditer(r"\d+,\d+", self.num[pos:]):
            nums = two_digits.group().split(",")

            str_before = self.num[:pos]
            res_len = len(nums[0]) + len(nums[1]) + len("[,]")

            str_after = self.num[pos + res_len:]

            # add to number before if any
            start = -1
            for item in re.finditer(r"\d+", str_before):
                new_num = int(nums[0]) + int(item.group())
                start = item.start()
                end = item.end()

            if start != -1:
                str_before = str_before[:start] + str(
                    new_num) + str_before[end:]

            # add to number after if any
            start = -1
            for item in re.finditer(r"\d+", str_after):

                new_num = int(nums[1]) + int(item.group())
                start = item.start()
                end = item.end()
                break

            if start != -1:
                str_after = str_after[:start] + str(new_num) + str_after[end:]

            self.num = f"{str_before}0{str_after}"
            return

    def split_num(self):
        """ Split digits > 10 """
        for item in re.finditer(r"\d{2,}", self.num):

            num_down = str(floor(int(item.group()) / 2))
            num_up = str(ceil(int(item.group()) / 2))
            self.num = self.num[:item.start(
            )] + f"[{str(num_down)},{str(num_up)}]" + self.num[item.end():]

            return 1

        return 0

    def reduce_num(self):
        """ Do the reduction """

        done_action = 1

        while done_action:
            done_action = 0
            bracket_count = 0

            for pos, char in enumerate(self.num):
                if char == "]":
                    bracket_count -= 1
                    continue

                if char == "[":
                    bracket_count += 1

                # can explode?
                if bracket_count == 5:
                    done_action = 1
                    self.explode(pos=pos)
                    break

            if done_action:
                continue

            done_action = self.split_num()

    def calculate_magnitude(self):
        """ Do the recursive calc """

        done_action = 1

        while done_action:
            done_action = 0

            for item in re.finditer(r"\d+,\d+", self.num):
                done_action = 1

                nums = item.group().split(",")
                result = int(nums[0]) * 3 + int(nums[1]) * 2

                self.num = self.num[:item.start() -
                                    1] + f"{result}" + self.num[item.end() +
                                                                1:]
                break

        return int(self.num)

    def add_all(self):
        """ Do the main task """

        self.num = self.lines[0]
        for line in self.lines[1:]:
            self.num = self.num + f",{line}]"
            self.num = "[" + self.num
            self.reduce_num()

    def compute_pairs(self):
        """ Do the main task """

        max_mag = 0

        for first, second in permutations(self.lines, 2):
            self.num = first
            self.num = self.num + f",{second}]"
            self.num = "[" + self.num
            self.reduce_num()
            new_mag = self.calculate_magnitude()
            if new_mag > max_mag:
                max_mag = new_mag

        print(max_mag)


def test_day_18():
    """ Run the tests """

    aoc = AoC18("input18_test1")
    aoc.add_all()
    aoc.calculate_magnitude()

    assert aoc.num == '1384'


def main():
    """ Run the exercise """
    aoc = AoC18("input18")
    # aoc.reduce_num()
    aoc.add_all()
    print(aoc.calculate_magnitude())
    aoc.compute_pairs()


if __name__ == "__main__":
    main()
