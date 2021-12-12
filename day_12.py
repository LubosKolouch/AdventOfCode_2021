#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Advent of Code 2021 Day 12 """

from collections import Counter
import networkx as nx


class Passage:
    """ Day 12 AoC """
    def __init__(self, in_file: str):
        self.g = nx.Graph()
        with open(in_file, "r") as file:
            lines = [line.strip() for line in file]
            for line in lines:
                node_from, node_to = line.split('-')
                self.g.add_edge(node_from, node_to)

    def get_repeated_small(self, path):
        """ Count the number of lower chars """

        counter = Counter(path)

        for item, value in counter.items():
            if item.islower() and value == 2:
                return item

        return None

    def get_paths_count(self, part: int):
        """ Find out the paths """

        all_paths = [["start"]]
        complete_paths = []

        changed_path = True
        while changed_path:
            changed_path = False

            for path in all_paths:
                # go through all available paths

                all_paths.remove(path)
                for possible_step in self.g.edges(path[-1]):

                    current_step, next_step = possible_step

                    if next_step == "start":
                        continue

                    # part 1
                    if part == 1 and next_step.islower() and next_step in path:
                        continue

                    # part 2
                    if part == 2 and next_step.islower():
                        repeated_char = self.get_repeated_small(path)

                        if repeated_char:

                            # have already something twice
                            # is it this one?
                            if repeated_char == next_step:
                                continue

                            # is the new one already there?
                            if next_step in path:
                                continue

                    changed_path = True
                    new_path = path.copy()
                    new_path.append(next_step)

                    if next_step == "end":
                        complete_paths.append(new_path)
                    else:
                        all_paths.append(new_path)

        return len(complete_paths)


def test_day_11():
    """ Run the tests """

    passage = Passage("input12_test")
    assert passage.get_paths_count(part=1) == 10
    assert passage.get_paths_count(part=2) == 36


def main():
    """ Run the exercise """
    passage = Passage("input12")
    print(passage.get_paths_count(part=1))
    print(passage.get_paths_count(part=2))


if __name__ == "__main__":
    main()
