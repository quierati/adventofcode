#!/usr/bin/env python3
import sys

import numpy as np


def process():
    with open(sys.argv[1]) as f:
        data = [ 
            list(
                map(int, line.replace(' -> ', ',').strip().split(','))
            ) for line in f ]
    return data


def execute():
    matrix = np.zeros([999, 999], dtype=int)
    data = process()
    for col,lin,col2,lin2  in data:
        if col == col2 or lin == lin2:
            c = col
            if col < col2:
                c = slice(col, col2+1)
            elif col2 < col:
                c = slice(col2, col+1)
            l = lin
            if lin < lin2:
                l = slice(lin, lin2+1)
            elif lin2 < lin:
                l = slice(lin2, lin+1)
            matrix[l, c] += 1
    print(f'My puzzle answer is: {(matrix > 1).sum()}')


if __name__ == '__main__':
    execute()
