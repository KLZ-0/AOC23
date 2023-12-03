import re
import sys
from collections import defaultdict

inp = [l.strip() for l in sys.stdin.readlines()]
n = len(inp[0])
ln = len(inp)

num_re = re.compile(r"(\d+)")
symb = re.compile(r"([^\d.])")

starloc = defaultdict(list)


def mark_stars(it, line_n, offset, num):
    found_any = False
    for s in it:
        if s.groups()[0] == "*":
            starloc[line_n, offset+s.span()[0]].append(num)
        found_any = True
    return found_any


def is_part(line_n, span, num):
    if span[0] > 0:
        span[0] -= 1
    if span[1] < n:
        span[1] += 1

    found = False
    if mark_stars(symb.finditer(inp[line_n][span[0]:span[1]]), line_n, span[0], num):
        found = True
    if line_n > 0 and mark_stars(symb.finditer(inp[line_n-1][span[0]:span[1]]), line_n-1, span[0], num):
        found = True
    if line_n < ln - 1 and mark_stars(symb.finditer(inp[line_n+1][span[0]:span[1]]), line_n+1, span[0], num):
        found = True

    return found


def solve1():
    sm = 0
    for line_n, l in enumerate(inp):
        for i in num_re.finditer(l):
            if is_part(line_n, list(i.span()), num := int(i.groups()[0])):
                sm += num
    return sm


def solve2():
    return sum([v[0] * v[1] for k, v in starloc.items() if len(v) == 2])


if __name__ == '__main__':
    print(f"Part 1: {solve1()}")
    print(f"Part 2: {solve2()}")
