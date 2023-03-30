# https://atcoder.jp/contests/pakencamp-2022-day1/tasks/pakencamp_2022_day1_a

X, Y = [int(x) for x in input().split()]


def solve(X: int, Y: int):
    result = (X != 0) + (Y != 0)
    print(result)


solve(X, Y)
