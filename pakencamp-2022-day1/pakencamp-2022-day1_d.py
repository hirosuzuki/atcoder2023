# https://atcoder.jp/contests/pakencamp-2022-day1/tasks/pakencamp_2022_day1_d

N, K = [int(x) for x in input().split()]


def solve(N: int, K: int):
    y = min(N // 3, N - K)
    c = K
    for i in range(1, N + 1):
        if c == 0:
            break
        if i % 3 == 0 and y > 0:
            y -= 1
        else:
            print(i, end=" ")
            c -= 1
    print()


solve(N, K)
