# https://atcoder.jp/contests/abc302/tasks/abc302_d

from typing import List

N, M, D = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]


def solve(N: int, M: int, D: int, A: List[int], B: List[int]):
    a = sorted(A, reverse=True)
    b = sorted(B, reverse=True)
    # print(a)
    # print(b)
    ai = 0
    bi = 0
    while ai < N and bi < M:
        # print(ai, bi, a, b)
        if abs(a[ai] - b[bi]) <= D:
            print(a[ai] + b[bi])
            return
        if a[ai] > b[bi]:
            ai += 1
        else:
            bi += 1

    print(-1)


solve(N, M, D, A, B)
