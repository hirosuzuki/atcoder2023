# https://atcoder.jp/contests/abc285/tasks/abc285_e

from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):

    dp: List[int] = [0] * N

    for i in range(1, N):
        r = sum(A[: (i + 1) // 2] + A[: i // 2])
        for j in range(1, (i + 1) // 2):
            r = max(r, dp[j] + dp[i - 1 - j])
        dp[i] = r

    print(dp[N - 1])


solve(N, A)
