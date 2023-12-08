import re
import sys
from typing import List

num_re = re.compile(r"(\d+)")
num_pair_re = re.compile(r"(\d+ \d+)")

blocks = [l.strip() for l in sys.stdin.read().split("\n\n")]


class Range:
    start: int
    size: int
    flag: bool = False

    def __init__(self, line: (str, tuple)):
        if isinstance(line, tuple):
            self.start = line[0]
            self.size = line[1] - line[0]
        else:
            if " " in line:
                self.start, self.size = map(int, line.split(" "))
            else:
                self.start = int(line)
                self.size = 1

    def __lt__(self, other):
        return self.start < other.start

    def __str__(self):
        return f"Range({self.start, self.size})"

    @property
    def end(self):
        return self.start + self.size - 1


class RangeMapping:
    src: Range
    dest: Range
    size: int

    def __init__(self, line: str):
        dest, src, size = map(int, line.split())
        self.src = Range(f"{src} {size}")
        self.dest = Range(f"{dest} {size}")
        self.size = size

    def __str__(self):
        return f"RangeMapping({self.src, self.dest, self.size})"

    def map(self, ranges: List[Range]) -> List[Range]:
        src = self.src
        dest = self.dest
        new_ranges = []

        for r in ranges:
            if r.flag:
                new_ranges.append(r)
                continue

            # no mapping
            if (r.start < src.start and r.end < src.start) or (r.start > src.end):
                new_ranges.append(r)
                continue

            # start
            if r.start < src.start <= r.end:
                new_ranges.append(Range((r.start, src.start - 1)))

            # intersection
            new_pair = (max(r.start, src.start), min(r.end, src.end))
            map_pair = tuple(dest.start + (x - src.start) for x in new_pair)
            tmp = Range(map_pair)
            tmp.flag = True
            new_ranges.append(tmp)

            # end
            if r.end > src.end:
                new_ranges.append(Range((src.end + 1, r.end)))

        return new_ranges


class MappingLayer:
    mappings = List[RangeMapping]

    def __init__(self, lines: List[str]):
        self.mappings = [RangeMapping(l) for l in lines]

    def map(self, ranges: List[Range]) -> List[Range]:
        for r in ranges:
            r.flag = False

        for mapping in self.mappings:
            ranges = mapping.map(ranges)

        return ranges

        # return x


maps = {u[0]: (u[1], MappingLayer(t[1:])) for l in blocks[1:] if (t := l.split("\n")) and (u := t[0].strip(" map:").split("-to-"))}


def iter_map(regex):
    current_nums = list(map(Range, regex.findall(blocks[0])))
    key = "seed"
    while key != "location":
        key, mapping_layer = maps[key]
        current_nums = mapping_layer.map(current_nums)
    return current_nums


def solve1():
    return min(iter_map(num_re)).start


def solve2():
    return min(iter_map(num_pair_re)).start


if __name__ == '__main__':
    print(f"Part 1: {solve1()}")
    print(f"Part 2: {solve2()}")
