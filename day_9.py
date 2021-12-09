#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
import numpy as np


class Smoke:
    """ Day 9 AoC """
    def __init__(self, in_file: str):
        self.map = np.genfromtxt(in_file, delimiter=1, dtype=int)
        self.x_max = 0
        self.y_max = 0
        self.lows = []

    @property
    def count_low_points(self):
        """ Part 1 """

        min_sum = 0
        self.x_max = len(self.map)
        self.y_max = len(self.map[0])

        for i in range(self.x_max):
            for j in range(self.y_max):

                my_min = self.map[i][j] + 1

                if i > 0:
                    my_min = min(my_min, self.map[i - 1][j])

                if i < self.x_max - 1:
                    my_min = min(my_min, self.map[i + 1][j])

                if j > 0:
                    my_min = min(my_min, self.map[i][j - 1])

                if j < self.y_max - 1:
                    my_min = min(my_min, self.map[i][j + 1])

                if self.map[i][j] < my_min:
                    self.lows.append((i, j))
                    min_sum += self.map[i][j] + 1
        return min_sum

    def fill_basin(self, basin):
        """ Fill the basin and get size """

        basin_deque = deque([basin])

        basin_points = dict()
        while 1:
            try:
                (x, y) = basin_deque.pop()
            except IndexError:
                break

            if basin_points.get((x, y), 0) == 1:
                continue
            basin_points[(x, y)] = 1

            if (x > 0) and self.map[x - 1][y] != 9:
                basin_deque.append((x - 1, y))

            if (x < self.x_max - 1) and self.map[x + 1][y] != 9:
                basin_deque.append((x + 1, y))

            if (y > 0) and self.map[x][y - 1] != 9:
                basin_deque.append((x, y - 1))

            if (y < self.y_max - 1) and self.map[x][y + 1] != 9:
                basin_deque.append((x, y + 1))

        return len(basin_points.keys())

    @property
    def get_largest_basin(self):
        """ Find out the largest basin"""

        min_sizes = dict()
        for basin in self.lows:
            min_sizes[basin] = self.fill_basin(basin=basin)

        largest_basins = sorted(min_sizes.values(), reverse=True)[:3]

        result = 1
        for item in largest_basins:
            result *= item

        return result


def test_day_9():
    """ Run the tests """

    part1 = Smoke("input9_test")
    assert part1.count_low_points == 15

    assert part1.get_largest_basin == 1134


def main():
    part1 = Smoke("input9")
    print(f"Part1: {part1.count_low_points}")
    print(f"Part1: {part1.get_largest_basin}")


if __name__ == "__main__":
    main()
