#!/usr/bin/env python3
from collections import Counter
import sys

data = None
input_file = sys.argv[1]
size = None


def process():
    global data,size
    with open(input_file) as f:
        data = [ value.strip() for value in f ]
        size = len(data[0])


def most_common(loc):
    return Counter([ item[loc] for item in data ]).most_common(1)[0][0]


def least_common(loc):
    return Counter([ item[loc] for item in data ]).most_common()[-1][0]


def bin2dec(value):
    value = "".join(value)
    return int(value, 2)


def execute():
    process()
    most = [ most_common(i) for i in range(size) ]
    least = [ least_common(i) for i in range(size) ]
    print(f'My puzzle answer is: {bin2dec(most)*bin2dec(least)}')


if __name__ == '__main__':
    execute()
