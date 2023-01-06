# https://atcoder.jp/contests/abc281/tasks/abc281_c

from typing import List

N, T = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

def solve(N: int, T: int, A: List[int]):
    ts = sum(A)
    t = T % ts
    for i, a in enumerate(A):
        if t < a:
            print(i + 1, t)
            return
        t -= a

solve(N, T, A)
