# https://atcoder.jp/contests/abc299/tasks/abc299_d

from sys import stdout

N = int(input())


def solve(N: int):
    lo = 1
    hi = N
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        print("?", mid)
        # stdout.flush()
        ans = int(input())
        if ans == 0:
            lo = mid
        else:
            hi = mid

    print("!", lo)
    # stdout.flush()


solve(N)
