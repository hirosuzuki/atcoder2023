# https://atcoder.jp/contests/abc286/tasks/abc286_a

from typing import List

N, P, Q, R, S = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, P: int, Q: int, R: int, S: int, A: List[int]):
    print(*A[: P - 1], *A[R - 1 : S], *A[Q : R - 1], *A[P - 1 : Q], *A[S:])


solve(N, P, Q, R, S, A)
