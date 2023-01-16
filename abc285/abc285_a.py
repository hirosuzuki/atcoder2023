# https://atcoder.jp/contests/abc285/tasks/abc285_a

a, b = [int(x) for x in input().split()]


def solve(a: int, b: int):
    result = (b == a * 2) or (b == a * 2 + 1)
    print(["No", "Yes"][result])


solve(a, b)
