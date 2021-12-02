#!/usr/bin/env python3

aim = 0
h_pos,v_pos = (0, 0)


def navigate(command, value):
    global aim,h_pos,v_pos
    if command == 'forward':
        h_pos += int(value)
        v_pos += aim*int(value)
    elif command == 'up':
        aim -= int(value)
    elif command == 'down':
        aim += int(value)


def process(input_file):
    with open(input_file) as f:
        for value in f:
            yield value.strip().split()


def execute(input_file):
    data = process(input_file)
    for item in data:
        command, value = item
        navigate(command, value)


    print(f'Aim: {aim}\nPosition: (horizontal={h_pos}, depth={v_pos})')
    print(f'My puzzle answer is: {h_pos*v_pos}')


if __name__ == '__main__':
    import sys
    execute(sys.argv[1])   
