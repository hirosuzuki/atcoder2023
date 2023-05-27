# https://atcoder.jp/contests/abc301/tasks/abc301_b

from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    result: List[int] = []
    result.append(A[0])
    for x in A[1:]:
        c = result[-1]
        while abs(c - x) != 1:
            if c > x:
                c -= 1
            else:
                c += 1
            result.append(c)
        result.append(x)
    print(*result)


solve(N, A)
