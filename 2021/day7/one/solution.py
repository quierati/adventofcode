#!/usr/bin/env python3
import statistics

def process():
    import sys
    with open(sys.argv[1]) as f:
        data = list(map(int, f.readline().strip().split(',')))
    return data


def execute():
    subs = process()
    median = int(statistics.median(subs))
    fuel = sum([ abs(crab - median)  for crab in subs ])
    print(f'My puzzle answer is: {fuel}')


if __name__ == '__main__':
    execute()
