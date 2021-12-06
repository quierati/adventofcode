#!/usr/bin/env python3
import numpy as np


def process():
    import sys
    with open(sys.argv[1]) as f:
        data = [ 
            map(int, item.replace(' -> ', ',').strip().split(','))
            for item in f ]
        return data


def execute():
    data = process()
    matrix = np.zeros([1000, 1000], dtype=int)
    matrix_diagonal = np.zeros([1000, 1000], dtype=int)

    for x1,y1,x2,y2 in data:
        if y1 == y2:
            i = slice(min(x1, x2), max(x1, x2)+1)
            matrix[y1, i] += 1
        elif x1 == x2:
            i = slice(min(y1, y2), max(y1, y2)+1)
            matrix[i, x1] += 1
        else:
            x_diag = range(y1, y2+1) if y1 < y2 else range(y1, y2-1, -1)
            y_diag = range(x1, x2+1) if x1 < x2 else range(x1, x2-1, -1)
            for x, y in zip(x_diag, y_diag):
               matrix_diagonal[x, y] += 1


    print(f'My puzzle answer is: {((matrix+matrix_diagonal) > 1).sum()}')


if __name__ == '__main__':
    execute()
