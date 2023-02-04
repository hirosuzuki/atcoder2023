# https://atcoder.jp/contests/abc270/tasks/abc270_d

from typing import List, Tuple

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, K: int, A: List[int]):
    dp: List[Tuple[int, int]] = []
    for i in range(N + 1):
        t, s = 0, 0
        for x in A:
            if i - x >= 0:
                t1, s1 = dp[i - x][1] + x, dp[i - x][0]
                if t1 > t:
                    t, s = t1, s1
        dp.append((t, s))

    print(dp[N][0])


solve(N, K, A)
