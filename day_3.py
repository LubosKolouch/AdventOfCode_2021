#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Advent Of Code 2021 Day 3"""

import pandas as pd


class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        self.keep_value = {1: '0', 0: '1'}
        self.diag_report = None
        self.split_pd = None
        self.methods = {}
        self._init_methods()

    def _init_methods(self):
        """ Prepare methods for each move """
        self.methods['forward'] = self.forward
        self.methods['up'] = self.up
        self.methods['down'] = self.down
        self.methods['forward_aim'] = self.forward_aim
        self.methods['up_aim'] = self.up_aim
        self.methods['down_aim'] = self.down_aim

    def forward(self, step: int):
        """ Move the sub forward """
        self.horizontal += step

    def forward_aim(self, step: int):
        """ Move the sub forward """
        self.horizontal += step
        self.depth += self.aim * step

    def up(self, step: int):
        """ Move the sub up """
        self.depth -= step

    def up_aim(self, step: int):
        """ Move the sub up """
        self.aim -= step

    def down(self, step: int):
        """ Move the sub down """
        self.depth += step

    def down_aim(self, step: int):
        """ Move the sub down """
        self.aim += step

    @property
    def result_day2(self):
        """ Return the solution for Part1 and Part2 """
        return self.depth * self.horizontal

    def load_diag_report(self, input_file) -> None:
        """ Load the diagnostic report to numpy array """
        self.diag_report = pd.read_csv(input_file,
                                       header=None,
                                       dtype="string",
                                       na_filter=True)
        self.diag_report.columns = ['input']

    def create_split_pd(self):
        """ Split the pd into one character per column """
        self.split_pd = self.diag_report.copy()
        self.split_pd = self.split_pd.loc[:, 'input'].str.split('',
                                                                expand=True)

    def calc_gamma_epsilon(self) -> tuple:
        """ Calculate the Gamma and Epsilon rates """

        gamma = ''
        epsilon = ''

        for test_col in range(1, len(self.diag_report.loc[0, 'input']) + 1):
            most_common = self.split_pd.value_counts(subset=[test_col])

            gamma += most_common.index[0][0]
            epsilon += most_common.index[1][0]

        return int(gamma, 2), int(epsilon, 2)

    def get_filter_value(self, column: int, position: int, keep: str):
        """ Filter only rows where it matches the digit
            Position: 0 = gamma, 1 = epsilon """

        most_common = self.split_pd.value_counts(subset=[column])

        # if equal counts, return 0 or 1 depending what is asked
        if most_common.iloc[0] == most_common.iloc[1]:
            return keep

        return most_common.index[position][0]

    def get_oxygen_co2_rating(self, what: int):
        """ Calculate the oxygen rating
            what: 0 = oxygen, 1 = co2 """

        for test_col in range(1, len(self.diag_report.loc[0, 'input']) + 2):

            if len(self.split_pd) == 1:
                result_index = self.split_pd.index[0]
                result = self.diag_report.iloc[result_index, 0]
                return int(result, 2)

            filter_value = self.get_filter_value(column=test_col,
                                                 position=what,
                                                 keep=self.keep_value[what])

            self.split_pd = self.split_pd.loc[(
                self.split_pd.loc[:, test_col] == filter_value)]


def test_day_3():
    """ Run the tests for Day 3"""

    test_sub = Submarine()

    test_sub.load_diag_report("input3_test")
    test_sub.create_split_pd()
    assert len(test_sub.diag_report) == 12

    assert test_sub.split_pd.loc[0, 1] == '0'
    assert test_sub.split_pd.loc[0, 5] == '0'

    assert test_sub.calc_gamma_epsilon() == (22, 9)

    assert test_sub.get_filter_value(1, 0, 0) == '1'
    assert test_sub.get_oxygen_co2_rating(what=0) == 23
    test_sub.create_split_pd()

    assert test_sub.get_oxygen_co2_rating(what=1) == 10


def main():
    """ Do the daily tasks """
    part1 = Submarine()

    part1.load_diag_report("input3")
    part1.create_split_pd()
    gamma, epsilon = part1.calc_gamma_epsilon()
    print(f"Part1: {gamma*epsilon}")

    part2 = Submarine()
    part2.load_diag_report("input3")
    part2.create_split_pd()
    oxygen = part2.get_oxygen_co2_rating(what=0)
    part2.create_split_pd()

    co2 = part2.get_oxygen_co2_rating(what=1)

    print(f"Part2: {oxygen*co2}")


if __name__ == "__main__":
    main()
