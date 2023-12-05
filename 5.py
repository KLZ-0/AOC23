import re
import sys

num_re = re.compile(r"(\d+)")

blocks = [l.strip() for l in sys.stdin.read().split("\n\n")]

maps = {u[0]: (u[1], [list(map(int, n.split())) for n in t[1:]]) for l in blocks[1:] if (t := l.split("\n")) and (u := t[0].strip(" map:").split("-to-"))}


def map_num(x, mapping):
    for dest, src, size in mapping:
        if src <= x < src+size:
            return x - src + dest
    return x


def iter_map():
    source_nums = list(map(int, num_re.findall(blocks[0])))
    key = "seed"
    while key != "location":
        key, mapping = maps[key]
        source_nums = [map_num(x, mapping) for x in source_nums]
    return source_nums

def solve1():
    return min(iter_map())


if __name__ == '__main__':
    print(solve1())
