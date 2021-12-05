#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import re


class Lines:
    """ Hold the lines """
    def __init__(self):
        self.all_points_part1 = defaultdict(int)
        self.all_points_part2 = defaultdict(int)
        self.all_lines = {}

    def load_input(self, in_file):
        """ Load the txt with input """

        with open(in_file, "r") as in_text:
            for count, line in enumerate(in_text.readlines()):
                x1, y1, x2, y2 = list(map(int, re.findall(r"\d+", line)))
                self.all_lines[count] = {
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2
                }

    def load_all_points(self):
        """ Process all lines """

        for line, point in self.all_lines.items():

            if point['x2'] > point['x1']:
                x_range = range(point['x1'], point['x2'] + 1)
            else:
                x_range = range(point['x1'], point['x2'] - 1, -1)

            if point['y2'] > point['y1']:
                y_range = range(point['y1'], point['y2'] + 1)
            else:
                y_range = range(point['y1'], point['y2'] - 1, -1)

            if len(x_range) == 1:
                for y in y_range:
                    self.all_points_part1[x_range[0], y] += 1
                    self.all_points_part2[x_range[0], y] += 1

            elif len(y_range) == 1:
                for x in x_range:
                    self.all_points_part1[x, y_range[0]] += 1
                    self.all_points_part2[x, y_range[0]] += 1

            else:
                for distance in range(len(x_range)):
                    self.all_points_part2[x_range[distance],
                                          y_range[distance]] += 1

    @property
    def get_part1(self) -> int:
        """ Return number of intersects for straight lines """
        filtered = dict(
            filter(lambda elem: elem[1] > 1, self.all_points_part1.items()))

        return len(filtered)

    @property
    def get_part2(self) -> int:
        """ Return number of intersects for straight lines """
        filtered = dict(
            filter(lambda elem: elem[1] > 1, self.all_points_part2.items()))

        return len(filtered)


def test_day_5():
    """ Run the tests """

    lines = Lines()

    lines.load_input("input5_test")
    lines.load_all_points()

    assert lines.get_part1 == 5
    assert lines.get_part2 == 12


def main():
    lines = Lines()
    lines.load_input("input5")
    lines.load_all_points()
    print(f"Part1: {lines.get_part1}")
    print(f"Part2: {lines.get_part2}")


if __name__ == "__main__":
    main()
