import re
import sys
from collections import defaultdict
from typing import List

inp = [l.strip() for l in sys.stdin.readlines()]
chars1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
chars2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

num_re = re.compile(r" (\d+)")


def hand_type_1(hand: str):
    hs = set(hand)
    counts = {c: hand.count(c) for c in hs}

    if len(hs) == 1:
        return 6

    if len(hs) == 2:
        if max(counts.values()) == 4:
            return 5
        else:
            return 4

    if len(hs) == 3:
        if max(counts.values()) == 3:
            return 3
        else:
            return 2

    if len(hs) == 4:
        return 1

    return 0


def hand_type_2(hand):
    def is_fh(mmax, counts):
        if mmax != 3:
            return False
        if 'J' in hand:
            return all(v == 2 for k, v in counts.items() if k != 'J')
        return 2 in counts.values() and 3 in counts.values()

    counts = defaultdict(int)
    mmax = 0  # Declare mmax as a nonlocal variable

    for card in hand:
        counts[card] += 1
        if card != 'J':
            mmax = max(mmax, counts[card])

    mmax += counts['J']

    if is_fh(mmax, counts):
        return 3.5

    pairs = sum(1 for v in counts.values() if v == 2)

    if counts['J'] == 2:
        pairs -= 1

    if mmax == 2 and pairs == 0:
        pairs = 1

    if pairs == 2:
        mmax = 2.5

    return mmax


chars: List[str]
hand_type = callable


def hand_strength(hand: str):
    return (chars.index(c) for c in hand)


def get_rank(line):
    hand = line.split(" ")[0]
    return -hand_type(hand), *hand_strength(hand)


def solve1():
    global chars, hand_type
    chars = chars1
    hand_type = hand_type_1
    return sum([(r+1) * int(num_re.search(s).groups()[0]) for r, s in enumerate(sorted(inp, key=get_rank, reverse=True))])


def solve2():
    global chars, hand_type
    chars = chars2
    hand_type = hand_type_2
    return sum([(r + 1) * int(num_re.search(s).groups()[0]) for r, s in enumerate(sorted(inp, key=get_rank, reverse=True))])


if __name__ == '__main__':
    print(f"Part 1: {solve1()}")
    print(f"Part 2: {solve2()}")
