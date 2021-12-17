#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Advent of Code 2021 Day 17 """

import re


class Shot:
    """ Day 17 AoC """
    def __init__(self, in_file: str):
        with open(in_file, "r") as my_in:
            line = my_in.readline().strip()

        self.coords = list(map(int, re.findall(r"(-?\d+)", line)))

    def find_high_y_coords(self):

        max_y = -9999
        all_vel = 0

        for x_v in range(0, 300):
            for y_v in range(-200, 200):
                x = 0
                y = 0
                max_loc_y = 0
                x_loc_v = x_v
                y_loc_v = y_v
                while x <= self.coords[1] and y >= self.coords[2]:
                    x += x_loc_v
                    y += y_loc_v
                    if self.coords[0] <= x <= self.coords[1] and self.coords[
                            2] <= y <= self.coords[3]:
                        if max_loc_y > max_y:
                            max_y = max_loc_y
                        all_vel += 1
                        break

                    max_loc_y = max(y, max_loc_y)
                    if x_loc_v > 0:
                        x_loc_v -= 1
                    elif x_loc_v < 0:
                        x_loc_v += 1

                    y_loc_v -= 1
        return max_y, all_vel


def test_day_17():
    """ Run the tests """

    fire = Shot("input17_test")
    max_vel, shot_count = fire.find_high_y_coords()
    assert shot_count == 112

    assert max_vel == 45


def main():
    """ Run the exercise """
    fire = Shot("input17")
    print(fire.find_high_y_coords())


if __name__ == "__main__":
    main()
