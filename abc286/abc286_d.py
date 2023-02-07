# https://atcoder.jp/contests/abc286/tasks/abc286_d

from typing import List

N, X = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, X: int, AB: List[List[int]]):
    cs = [False] * (X + 1)
    cs[0] = True
    for a, b in AB:
        for i, c in enumerate(cs[:]):
            if not c:
                continue
            for j in range(1, b + 1):
                if i + j * a > X:
                    break
                cs[i + j * a] = True

    if cs[X]:
        print("Yes")
    else:
        print("No")


solve(N, X, AB)
