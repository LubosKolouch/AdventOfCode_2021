#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


class Syntax:
    """ Day 10 AoC """
    def __init__(self, in_file: str):

        self.map = []
        with open(in_file, "r") as lines:
            self.map = [line.strip() for line in lines]

        self.delims = {"(": ")", "[": "]", "{": "}", "<": ">"}
        self.scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
        self.scores_completion = {")": 1, "]": 2, "}": 3, ">": 4}

    @property
    def count_wrong_scores(self):
        """ Part 1 """

        wrong_sum = 0
        compl_sums = []

        for line in self.map:

            chars_deque = deque()
            for j in line:
                if j in self.delims.keys():
                    chars_deque.append(self.delims[j])
                    continue

                # check if the closing delimited is the right one
                if j != chars_deque.pop():
                    wrong_sum += self.scores[j]
                    chars_deque = deque()
                    break

            compl_sum = 0

            if not chars_deque:
                continue
            for char in reversed(chars_deque):
                compl_sum *= 5
                compl_sum += self.scores_completion[char]

            compl_sums.append(compl_sum)

        middle_sum = sorted(compl_sums)[len(compl_sums) // 2]

        return wrong_sum, middle_sum


def test_day_10():
    """ Run the tests """

    part1 = Syntax("input10_test")

    wrong_sum, middle_sum = part1.count_wrong_scores
    assert wrong_sum == 26397
    assert middle_sum == 288957


def main():
    part1 = Syntax("input10")

    wrong_sum, middle_sum = part1.count_wrong_scores
    print(f"Part1: {wrong_sum}")
    print(f"Part2: {middle_sum}")


if __name__ == "__main__":
    main()
