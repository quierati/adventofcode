#!/usr/bin/env python3

def process():
    import sys
    with open(sys.argv[1]) as f:
        data = [ line.strip().split('|')[1].strip() 
                    for line in f.readlines() ]
    return data


def execute():
   data = process()
   resp = [ 1 for output in data 
                for item in output.split() 
                    if len(item) in (2, 3, 4, 7) ] 
   print(f'My puzzle answer is: {resp}')


if __name__ == '__main__':
    execute()
