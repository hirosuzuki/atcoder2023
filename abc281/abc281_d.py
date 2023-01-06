# https://atcoder.jp/contests/abc281/tasks/abc281_d

from typing import List

N, K, D = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

def solve(N: int, K: int, D: int, A: List[int]):
    # dp[N][K][D]

    dp = [[[-1 for _ in range(D)] for _ in range(K + 1)] for _ in range(N + 1)]

    dp[0][0][0] = 0

    for n in range(1, N + 1):
        x = A[n - 1]
        for k in range(0, K + 1):
            for d in range(D):
                dp[n][k][d] = dp[n - 1][k][d]
                if k > 0:
                    if dp[n - 1][k - 1][(d - x) % D] >= 0:
                        dp[n][k][d] = max(dp[n][k][d], dp[n - 1][k - 1][(d - x) % D] + x)

    result = dp[N][K][0]
    print(result)

solve(N, K, D, A)
