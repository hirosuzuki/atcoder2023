# https://atcoder.jp/contests/abc275/tasks/abc275_b

A, B, C, D, E, F = [int(x) for x in input().split()]


def solve(A: int, B: int, C: int, D: int, E: int, F: int):
    M = 998244353
    print((A * B * C - D * E * F) % M)


solve(A, B, C, D, E, F)
