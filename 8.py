import math
import re
import sys

inp = [l.strip() for l in sys.stdin.readlines()]

imap = {"R": 1, "L": 0}
instr = [imap[letter] for letter in inp[0]]
maps = {t[0]: t[1].strip("()").split(", ") for l in inp[2:] if (t := l.split(" = "))}


def map_num(start, end):
    pos = start
    idx = 0
    count = 0
    while not pos.endswith(end):
        pos = maps[pos][instr[idx]]
        idx = (idx + 1) % len(instr)
        count += 1
    return count


def solve1():
    return map_num("AAA", "ZZZ")


def solve2():
    return math.lcm(*[map_num(k, "Z") for k in maps.keys() if k.endswith("A")])


if __name__ == '__main__':
    print(f"Part 1: {solve1()}")
    print(f"Part 2: {solve2()}")
