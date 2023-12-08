import re
import sys

inp = [l.strip() for l in sys.stdin.readlines()]

num_re = re.compile(r"(\d+)")


def do_race(time, dist):
    count = 0
    for i in range(time):
        speed = i
        time_left = time - i
        new_dist = time_left * speed
        if new_dist > dist:
            count += 1
    return count


def solve1():
    nums = [list(map(int, num_re.findall(l))) for l in inp]
    mul = 1
    for time, dist in zip(*nums):
        mul *= do_race(time, dist)
    return mul


def solve2():
    time, dist = [int(num_re.search(l.replace(" ", "")).groups()[0]) for l in inp]
    return do_race(time, dist)


if __name__ == '__main__':
    print(f"Part 1: {solve1()}")
    print(f"Part 2: {solve2()}")
