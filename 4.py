import re
import sys

inp = [l.strip() for l in sys.stdin.readlines()]

num_re = re.compile(r"(\d+)")


def get_common(line):
    winning, own = map(lambda x: set(map(int, num_re.findall(x))), line.split(":")[1].split("|"))
    return len(winning.intersection(own))


def solve_line(line):
    li = get_common(line)
    return 2 ** (li - 1) if li > 0 else 0


def solve1():
    return sum(map(solve_line, inp))


def solve2():
    tmp = [1] * len(inp)
    for i, line in enumerate(inp):
        for j in range(get_common(line), 0, -1):
            tmp[i + j] += tmp[i]
    return sum(tmp)


if __name__ == '__main__':
    print(f"Part 1: {solve1()}")
    print(f"Part 2: {solve2()}")
