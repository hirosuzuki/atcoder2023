# https://atcoder.jp/contests/abc289/tasks/abc289_d

from typing import List

N = int(input())
A = [int(x) for x in input().split()]
M = int(input())
B = [int(x) for x in input().split()]
X = int(input())


def solve(N: int, A: List[int], M: int, B: List[int], X: int):
    cs: List[int] = [0] * (X + 1)
    for n in B:
        cs[n] = -1
    cs[0] = 1
    for i in range(X):
        if cs[i] == 1:
            for d in A:
                p = i + d
                if p <= X and cs[p] == 0:
                    cs[p] = 1
    if cs[X] == 1:
        print("Yes")
    else:
        print("No")


solve(N, A, M, B, X)
