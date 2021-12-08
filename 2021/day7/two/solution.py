#!/usr/bin/env python3
import statistics

def process():
    import sys
    with open(sys.argv[1]) as f:
        data = list(map(int, f.readline().strip().split(',')))
    return data


def execute():
    subs = process()
    mean = int(statistics.mean(subs))
    fuel = 0
    for crab in subs:
        dist = abs(crab - mean)
        fuel += sum(x for x in range(dist+1))
    print(f'My puzzle answer is: {fuel}')


if __name__ == '__main__':
    execute()
