#!/usr/bin/env python3

from sys import argv
from math import log

ops = 0x2B2D2F2C

def func(a, b):
    return '\n'.join(
        (lambda r: f'{a} {f} {b} = {r}')(eval(f'{a}{f}{b}'))
        for f in ops.to_bytes((int(log(ops, 16)) + 1) // 2, 'big').decode())
    

if __name__ == '__main__':
    a, b = map(int, argv[1:])
    print(func(a, b))
