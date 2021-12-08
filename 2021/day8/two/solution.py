#!/usr/bin/env python3
from itertools import permutations

segments = {
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
    0: "abcefg",
}
lookup = { frozenset(value): str(key) for key, value in segments.items() }
translations = [str.maketrans("".join(s), "abcdefg") for s in permutations("abcdefg", 7)]


def process():
    import sys
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            yield line.strip().split('|')


def execute():
    resp = 0
    for patterns,outputs in process():
        for t in translations:
            if all(frozenset(pattern.translate(t)) in lookup 
                    for pattern in patterns.strip().split()):
                break
        code = "".join([lookup[frozenset(output.translate(t))] 
                    for output in outputs.strip().split()])
        resp += int(code)
    print(f'My puzzle answer is: {resp}')


if __name__ == '__main__':
    execute()
