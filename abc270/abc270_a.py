# https://atcoder.jp/contests/abc270/tasks/abc270_a

A, B = [int(x) for x in input().split()]


def solve(A: int, B: int):
    print(A | B)


solve(A, B)
