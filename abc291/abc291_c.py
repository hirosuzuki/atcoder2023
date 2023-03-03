# https://atcoder.jp/contests/abc291/tasks/abc291_c

from typing import Set, Tuple

N = int(input())
S = input()


def solve(N: int, S: str):
    def check() -> bool:
        x, y = 0, 0
        ps: Set[Tuple[int, int]] = set()
        ps.add((x, y))
        dx = {"U": 0, "D": 0, "R": 1, "L": -1}
        dy = {"U": 1, "D": -1, "R": 0, "L": 0}
        for c in S:
            x, y = x + dx[c], y + dy[c]
            if (x, y) in ps:
                return True
            ps.add((x, y))
        return False

    if check():
        print("Yes")
    else:
        print("No")


solve(N, S)
