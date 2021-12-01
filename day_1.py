#!/usr/bin/env python
# coding: utf-8
""" Advent Of Code 2021 - Day 1 """

import pandas as pd

signals = pd.read_csv('input_1', header=None)
signals.columns = ['1']

signals['diff'] = signals['1'].diff()
increased = signals.loc[(signals['diff'] > 0)]
print(f"Part1: {len(increased)}")

signals['2'] = signals['1'].shift(-1)
signals['3'] = signals['2'].shift(-1)

signals['sum'] = signals['1'] + signals['2'] + signals['3']
signals['sum_diff'] = signals['sum'].diff()
increased_sums = signals.loc[(signals['sum_diff'] > 0)]

print(f"Part2: {len(increased_sums)}")
