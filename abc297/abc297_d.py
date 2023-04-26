# https://atcoder.jp/contests/abc297/tasks/abc297_d

A, B = [int(x) for x in input().split()]


def solve(A: int, B: int):
    b, a = sorted([A, B])

    result = -1
    while b:
        a, b, result = b, a % b, result + a // b

    print(result)


solve(A, B)
