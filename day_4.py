#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from collections import deque, defaultdict
import re
import sys
import numpy as np


class BingoCollection:
    """ holds the Bingo cards and statuses """
    def __init__(self):
        self.cards = []
        self.all_nums = defaultdict(list)
        self.draw_queue = deque()
        self.boards_won = {}

    def load_input(self, in_file):
        """ Load the board and the queue """

        with open(in_file, "r") as file:
            self.draw_queue = list(
                map(int,
                    file.readline().strip().split(sep=',')))

            card_num = -1
            row_num = 0

            lines = [line.strip() for line in file]
            for line in lines:
                logging.warning(line)
                if line == "":
                    logging.warning("separator")
                    card_num += 1

                    new_card = BingoCard(card_id=card_num)
                    self.cards.append(new_card)
                    row_num = 0
                else:
                    logging.warning("Processing")
                    row = list(map(int, re.split(r"\s+", line)))
                    logging.warning(row)

                    for pos, num in enumerate(row):
                        # list(map(int, re.split(r'\s+', line)))):
                        self.all_nums[num].append(
                            f"{card_num} {row_num} {pos}")
                        self.cards[card_num].orig_nums[row_num][pos] = num
                    row_num += 1

    def check_any_card_win(self):
        """ Check if any card has won """

        for card in self.cards:
            if self.boards_won.get(card.card_id, -1) != -1:
                continue
            if card.is_complete:
                return card.card_id

        return -1

    def process_queue(self, task: int = 1):
        """ Go through the drawn numbers """

        logging.warning(self.cards)
        for num in self.draw_queue:
            logging.warning("********* Drawn num %s", num)
            cards = self.all_nums[num]
            logging.warning(cards)
            for card in cards:
                card_id, row_id, col_id = list(map(int, re.split(r'\s', card)))
                logging.warning("card_id row_id col_id %s %s %s", card_id,
                                row_id, col_id)
                self.cards[card_id].board[row_id][col_id] = 1
                win_card = self.check_any_card_win()
                if win_card != -1:
                    self.boards_won[win_card] = 1
                    logging.debug("Boards won so far: %s",
                                  len(self.boards_won))
                    if task == 1 or len(self.boards_won) == len(self.cards):
                        logging.warning("Card %s won", win_card)
                        self.cards[win_card].calculate_score()
                        logging.warning("Part 1: %s",
                                        self.cards[win_card].score * num)
                        return self.cards[win_card].score * num
        return None


class BingoCard:
    """ Holds one Bingo card """
    def __init__(self, card_id: int):
        self.board = np.zeros((5, 5), dtype=int)
        self.orig_nums = np.empty((5, 5), dtype=int)
        self.card_id = card_id
        self.score = 0
        logging.warning(self.board)

    @property
    def is_complete(self):
        """ Checks if the board is complete """
        logging.warning(self.board)
        for i in range(5):
            logging.warning("row col %s", i)
            row_ones = np.count_nonzero(self.board[i, :])
            col_ones = np.count_nonzero(self.board[:, i])
            logging.warning("row_ones: %s", row_ones)
            logging.warning("col ones: %s", col_ones)

            if row_ones == 5 or col_ones == 5:
                return True

        return False

    def calculate_score(self):
        """ Calculate the non empty score """

        for i in range(5):
            for j in range(5):
                if self.board[i][j] == 0:
                    self.score += self.orig_nums[i][j]


def test_day_5_part1():
    """ Tests for Day 5 """
    bingocard = BingoCard(card_id=0)
    assert bingocard.is_complete == False

    for i in range(5):
        bingocard.board[0][i] = 1

    assert bingocard.is_complete == True

    for i in range(5):
        bingocard.board[0][i] = 0
        bingocard.board[i][0] = 1

    assert bingocard.is_complete == True

    coll = BingoCollection()
    coll.load_input('input4_test')

    assert len(coll.all_nums) == 27

    assert coll.process_queue() == 4512


def test_day_5_part2():
    """ Tests for Day 5 """
    coll_2 = BingoCollection()
    coll_2.load_input('input4_test')
    assert coll_2.process_queue(task=2) == 1924


def main():
    """ Do the daily tasks """
    logging.basicConfig(
        format="%(asctime)s %(levelname)s:"
        "[%(filename)s:%(lineno)s - %(funcName)20s() ] "
        "%(message)s",
        #                level=logging.WARNING,
        level=logging.ERROR,
        datefmt="%H:%M:%S",
        stream=sys.stderr,
    )

    coll_task1 = BingoCollection()
    coll_task1.load_input('input4')
    print(f"Task 1 : {coll_task1.process_queue()}")

    coll_task2 = BingoCollection()
    coll_task2.load_input('input4')
    print(f"Task 2 : {coll_task2.process_queue(task=2)}")


if __name__ == "__main__":
    main()
