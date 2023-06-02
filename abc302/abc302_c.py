# https://atcoder.jp/contests/abc302/tasks/abc302_c

from itertools import permutations
from typing import List, Set, Tuple

N, M = [int(x) for x in input().split()]
S = [input() for _ in range(N)]


def solve(N: int, M: int, S: List[str]):
    ns: Set[Tuple[int, int]] = set()
    for i in range(N):
        for j in range(i + 1, N):
            r = sum([c1 != c2 for c1, c2 in zip(S[i], S[j])])
            if r <= 1:
                ns.add((i, j))
                ns.add((j, i))
    for r in permutations(list(range(N))):
        if all((r[i], r[i + 1]) in ns for i in range(N - 1)):
            print("Yes")
            return

    print("No")


solve(N, M, S)
