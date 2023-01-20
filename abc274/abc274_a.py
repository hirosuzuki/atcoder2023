# https://atcoder.jp/contests/abc274/tasks/abc274_a

A, B = [int(x) for x in input().split()]


def solve(A: int, B: int):
    print("%.3f" % (round(B * 1000 / A) / 1000))


solve(A, B)
