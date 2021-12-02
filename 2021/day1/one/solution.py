#!/usr/bin/env python3


def execute(input_file):
    counter = []
    with open(input_file) as f:
        previous = 0
        for current in f:
            current = int(current.strip())
            if not previous:
                previous = current
                continue
            counter.append(current > previous)
            previous = current

    print(f'My puzzle answer is: {sum(counter)}')


if __name__ == '__main__':
    import sys
    execute(sys.argv[1])
