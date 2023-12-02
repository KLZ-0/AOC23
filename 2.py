import re
import sys

colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

game_re = re.compile(r"Game (\d+): ")
color_re_template = r"(\d+) {}"
colors_re = {k: re.compile(color_re_template.format(k)) for k in colors.keys()}


def solve_line(line):
    for color, color_re in colors_re.items():
        if max(map(int, color_re.findall(line))) > colors[color]:
            return 0
    return int(game_re.search(line).groups()[0])


inp = sys.stdin.readlines()


def solve():
    print(sum([solve_line(l) for l in inp]))


if __name__ == '__main__':
    solve()
