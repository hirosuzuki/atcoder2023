# https://atcoder.jp/contests/abc299/tasks/abc299_b

from typing import List

N, T = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
R = [int(x) for x in input().split()]


def solve(N: int, T: int, C: List[int], R: List[int]):
    r1v, r1i = -1, -1
    r2v, r2i = R[0], 0
    for i in range(N):
        c, r = C[i], R[i]
        if c == T:
            if r > r1v:
                r1v, r1i = r, i
        if c == C[0]:
            if r > r2v:
                r2v, r2i = r, i

    if r1i == -1:
        print(r2i + 1)
    else:
        print(r1i + 1)


solve(N, T, C, R)
