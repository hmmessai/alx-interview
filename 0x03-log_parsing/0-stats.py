#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""
import sys

lines = sys.stdin


def read_n_lines(n):
    """Reads the given amount of lines from stdin"""
    return [sys.stdin.readline().rstrip() for _ in range(n)]


if __name__ == 'main':
    while lines:
        totalSize = 0
        count = 0
        codes = {'200': 0,
                '301': 0,
                '400': 0,
                '401': 0,
                '403': 0,
                '404': 0,
                '405': 0,
                '500': 0}
        lines = read_n_lines(10)
        while count < 10:
            line = lines[count]
            arg = line.split(" ")
            totalSize += int(arg[-1])
            for code in codes.keys():
                if code == arg[-2]:
                    codes[code] += 1
            count += 1

        print('File size: {}'.format(totalSize))
        for code, value in sorted(codes.items()):
            if value != 0:
                print('{}: {}'.format(code, value))
