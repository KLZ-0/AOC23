import re
import sys

inp = sys.stdin.readlines()

colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

game_re = re.compile(r"Game (\d+): ")
color_re_template = r"(\d+) {}"
colors_re = {k: re.compile(color_re_template.format(k)) for k in colors.keys()}


def part1(line: str) -> int:
    for color, color_re in colors_re.items():
        if max(map(int, color_re.findall(line))) > colors[color]:
            return 0
    return int(game_re.search(line).groups()[0])


def part2(line: str) -> int:
    mul = 1
    for color, color_re in colors_re.items():
        mul *= max(map(int, color_re.findall(line)))
    return mul


if __name__ == '__main__':
    print(f"Part 1: {sum(map(part1, inp))}")
    print(f"Part 2: {sum(map(part2, inp))}")
