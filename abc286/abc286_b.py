# https://atcoder.jp/contests/abc286/tasks/abc286_b

N = int(input())
S = input()


def solve(N: int, S: str):
    result = S.replace("na", "nya")
    print(result)


solve(N, S)
