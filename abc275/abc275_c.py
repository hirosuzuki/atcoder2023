# https://atcoder.jp/contests/abc275/tasks/abc275_c

from typing import List, Set, Tuple

S = [input() for _ in range(9)]


def solve(S: List[str]):
    xy: Set[Tuple[int, int]] = set()
    for x in range(9):
        for y in range(9):
            if S[y][x] == "#":
                xy.add((x, y))

    result = 0
    for x in range(9):
        for y in range(9):
            for dx in range(9):
                for dy in range(1, 9):
                    if dx == 0 and dy == 0:
                        continue
                    p1 = (x, y)
                    p2 = (x + dx, y + dy)
                    p3 = (x - dy, y + dx)
                    p4 = (x + dx - dy, y + dx + dy)
                    if (p1 in xy) and (p2 in xy) and (p3 in xy) and (p4 in xy):
                        result += 1

    print(result)


solve(S)
