import re
import sys

inp = sys.stdin.read().split()


def part1():
    pat = re.compile(r"^\D*(\d).*?(\d)?\D*$")
    pairs = [re.match(pat, n).groups() for n in inp]
    nums = [int(n1+n2) if n2 is not None else int(n1+n1) for n1, n2 in pairs]
    return sum(nums)


def part2():
    pat2 = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
    nm = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    nums = [int(nm[q[0]] + nm[q[-1]]) for n in inp if (q := pat2.findall(n))]
    return sum(nums)


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
