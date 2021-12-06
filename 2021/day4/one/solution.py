#!/usr/bin/env python3
from itertools import chain
import sys

import numpy as np


bingos = np.loadtxt(sys.argv[1], dtype=int, skiprows=1)
cards = list(range(0,500,5))
draw = np.loadtxt(sys.argv[1], dtype=int,delimiter=',', max_rows=1)
inc = 5


def uniq(np_array):
    return set(chain.from_iterable(np_array))


def check_column(card, draw):
    for column in range(5):
        c = uniq(bingos[:,column:column+1][card:card+inc])
        if len(draw & c) == inc:
            return True


def check_line(card, draw):
    for line in range(5):
        if len(draw & set(bingos[card+line])) == inc:
            return True


def filter_bingo(card, draw):
    c = [ bingos[card+pos] for pos in range(inc) ]
    return sum(uniq(c) - set(draw))


def execute():
    for pos in range(len(draw)):
        for card in cards:
            if check_line(card, set(draw[:pos])) or check_column(card, set(draw[:pos])):
                print(f'My puzzle answer is: {draw[pos-1] * filter_bingo(card, draw[:pos])}')
                return


if __name__ == '__main__':
    execute()

