#!/usr/bin/env python3


def counter(data):
    previous = 0 
    count = 0
    for values in data:
        current = sum(values)
        if not previous:
            previous = current
            continue
        if current > previous:
            count += 1
        previous = current
    return count


def process(input_file):
    with open(input_file) as f:
        data = []
        for value in f:
            data.append(int(value.strip()))
            if len(data) == 3:
                yield data
                data.pop(0)


def execute(input_file):
    data = process(input_file)
    total = counter(data)
    print(f'My puzzle answer is: {total}')


if __name__ == '__main__':
    import sys
    execute(sys.argv[1])
