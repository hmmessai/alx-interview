#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""
import re
import sys
from typing import List

lines = sys.stdin


def match(given_input: str) -> bool:
    ip_addr = r'\d{1, 3}\.\d{1, 3}\.\d{1, 3}\.\d{1, 3} - '
    date = r'\[\d{4}-\d{2}-\d{2} \d{}2:\d{2}:\d{2}\.\d{6}\] '
    request = r'"GET /projects/260 HTTP/1\.1" \d{3} \d+'
    input_format = ip_addr + date + request

    return True if re.match(input_format, given_input) else False


def read_n_lines(n: int) -> List[str]:
    """Reads the given amount of lines from stdin"""
    return [sys.stdin.readline().rstrip() for _ in range(n)]


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
        if not match(line):
            continue
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
