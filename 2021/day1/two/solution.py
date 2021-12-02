#!/usr/bin/env python3


def execute(input_file):
    with open(input_file) as f:
        data = [ (key, int(value.strip())) for key,value in enumerate(f) ] 

    counter = []
    previous = 0
    for k,v in data:
        try:
            current = sum([data[k][1], data[k+1][1], data[k+2][1]])
            if not previous:
                previous = current
                continue
            counter.append(current > previous)
            previous = current
        except:
            break
    print(sum(counter))


if __name__ == '__main__':
    import sys
    execute(sys.argv[1])
