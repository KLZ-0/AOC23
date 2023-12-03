import re
import sys

inp = [l.strip() for l in sys.stdin.readlines()]
n = len(inp[0])
ln = len(inp)

num_re = re.compile(r"(\d+)")
symb = re.compile(r"([^\d.])")


def is_part(line_n, span):
    if span[0] > 0:
        span[0] -= 1
    if span[1] < n:
        span[1] += 1

    if symb.search(inp[line_n][span[0]:span[1]]):
        return True
    if line_n > 0 and symb.search(inp[line_n-1][span[0]:span[1]]):
        return True
    if line_n < ln - 1 and symb.search(inp[line_n+1][span[0]:span[1]]):
        return True

    return False


def solve():
    sm = 0
    for line_n, l in enumerate(inp):
        for i in num_re.finditer(l):
            if is_part(line_n, list(i.span())):
                sm += int(i.groups()[0])
    return sm


if __name__ == '__main__':
    print(solve())
