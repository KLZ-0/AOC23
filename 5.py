import re
import sys
from typing import List

num_re = re.compile(r"(\d+)")
num_pair_re = re.compile(r"(\d+) (\d+)")

blocks = [l.strip() for l in sys.stdin.read().split("\n\n")]


class Range:
    start: int
    size: int

    def __init__(self, line: str):
        if " " in line:
            self.start, self.size = map(int, line.split(" "))
        else:
            self.start = int(line)
            self.size = 1

    def __lt__(self, other):
        return self.start < other.start

    def __str__(self):
        return f"Range({self.start, self.size})"


class RangeMapping:
    src: int
    dest: int
    size: int

    def __init__(self, line: str):
        dest, src, size = map(int, line.split())
        self.src = src
        self.dest = dest
        self.size = size

    def __str__(self):
        return f"RangeMapping({self.src, self.dest, self.size})"

    def map(self, x: Range):
        if self.src <= x.start < self.src + self.size:
            x.start = x.start - self.src + self.dest
            return True

        return False


class MappingLayer:
    mappings = List[RangeMapping]

    def __init__(self, lines: List[str]):
        self.mappings = [RangeMapping(l) for l in lines]

    def map(self, x: Range):
        for mapping in self.mappings:
            if mapping.map(x):
                return x

        return x


maps = {u[0]: (u[1], MappingLayer(t[1:])) for l in blocks[1:] if (t := l.split("\n")) and (u := t[0].strip(" map:").split("-to-"))}


def iter_map():
    source_nums = list(map(Range, num_re.findall(blocks[0])))
    key = "seed"
    while key != "location":
        key, mapping_layer = maps[key]
        source_nums = [mapping_layer.map(x) for x in source_nums]
    return source_nums

def solve1():
    return min(iter_map())


if __name__ == '__main__':
    print(solve1())
