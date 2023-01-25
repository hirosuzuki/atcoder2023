# https://atcoder.jp/contests/abc273/tasks/abc273_b

X, K = [int(x) for x in input().split()]


def solve(X: int, K: int):
    r = X
    for i in range(K):
        n = 10**i
        m = n * 10
        y = r // n % 10
        if y < 5:
            r = r // m * m
        else:
            r = (r // m + 1) * m
    print(r)


solve(X, K)
