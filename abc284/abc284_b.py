# https://atcoder.jp/contests/abc284/tasks/abc284_b

from typing import List

T = int(input())
N: List[int] = []
A: List[List[int]] = []

for _ in range(T):
    N.append(int(input()))
    A.append([int(x) for x in input().split()])


def solve(T: int, N: List[int], A: List[List[int]]):
    for xs in A:
        r = sum(x % 2 for x in xs)
        print(r)


solve(T, N, A)
