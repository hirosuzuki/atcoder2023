# https://atcoder.jp/contests/abc303/tasks/abc303_d

X, Y, Z = [int(x) for x in input().split()]
S = input()


def solve(X: int, Y: int, Z: int, S: str):
    dp = [[0] * (len(S) + 1) for _ in range(2)]
    dp[1][0] = float("inf")
    for i in range(len(S)):
        c = S[i]
        if c == "A":
            dp[0][i + 1] = min(dp[0][i] + Y, dp[1][i] + Z + Y)
            dp[1][i + 1] = min(dp[0][i] + Z + X, dp[1][i] + X)
        elif c == "a":
            dp[0][i + 1] = min(dp[0][i] + X, dp[1][i] + Z + X)
            dp[1][i + 1] = min(dp[0][i] + Z + Y, dp[1][i] + Y)
    print(min(dp[0][-1], dp[1][-1]))


solve(X, Y, Z, S)
