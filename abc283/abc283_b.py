# https://atcoder.jp/contests/abc283/tasks/abc283_b

from typing import List

N = int(input())
A = [int(x) for x in input().split()]
Q = int(input())
query = [[int(x) for x in input().split()] for x in range(Q)]

def solve(N: int, A: List[int], Q: int, query: List[List[int]]):
    xs = A[:]
    for q in query:
        if q[0] == 1:
            xs[q[1] - 1] = q[2]
        elif q[0] == 2:
            print(xs[q[1] - 1])

solve(N, A, Q, query)
