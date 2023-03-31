# https://atcoder.jp/contests/pakencamp-2022-day1/tasks/pakencamp_2022_day1_b

N, M = [int(x) for x in input().split()]


def solve(N: int, M: int):
    if N == 1:
        print(0)
        return

    if M == 1:
        print(-1)
        return

    result = ((N - 1) + (M - 1) - 1) // (M - 1)
    print(result)


solve(N, M)
