# https://atcoder.jp/contests/abc294/tasks/abc294_a


from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    result = [x for x in A if x % 2 == 0]
    print(*result)


solve(N, A)
