# https://atcoder.jp/contests/abc302/tasks/abc302_a

A, B = [int(x) for x in input().split()]


def solve(A: int, B: int):
    result = (A + B - 1) // B
    print(result)


solve(A, B)
