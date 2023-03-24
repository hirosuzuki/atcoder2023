# https://atcoder.jp/contests/abc294/tasks/abc294_c


from typing import List

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]


def solve(N: int, M: int, A: List[int], B: List[int]):
    C = sorted(A + B)
    cs = dict((v, i + 1) for i, v in enumerate(C))
    print(*[cs[x] for x in A])
    print(*[cs[x] for x in B])


solve(N, M, A, B)
