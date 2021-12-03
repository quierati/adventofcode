#!/usr/bin/env python3
from collections import Counter
from statistics import mode
import sys

input_file = sys.argv[1]
data = None
size = None


def search(pattern, pos):
    global data
    if pos:
        pattern = "".join([data[0][slice(pos)], pattern])
    data = [ item for item in data if item.startswith(pattern) ]


def process():
    global data,size
    with open(input_file) as f:
        data = [ value.strip() for value in f ]
        size = len(data[0])


def bit_criteria(pos):
    c = Counter([ item[pos] for item in data ])
    try:
        a,b = c.values()
        if a == b:
            return 1
    except:
        pass
    return int(c.most_common(1)[0][0])


def bin2dec(value):
    value = "".join(value)
    return int(value, 2)


def oxygen():
    process()
    for pos in range(size):
        if len(data) == 1:
            break
        who = bit_criteria(pos)
        search(str(who),pos)

    return bin2dec(data[0])


def co2():
    process()
    for pos in range(size):
        if len(data) == 1:
            break
        who = int(bit_criteria(pos) == False)
        search(str(who),pos)
    return bin2dec(data[0])
 

def execute():
    print(f'My puzzle answer is: {oxygen()*co2()}')


if __name__ == '__main__':
    execute()
