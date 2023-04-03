# https://atcoder.jp/contests/abc296/tasks/abc296_a

N = int(input())
S = input()


def solve(N: int, S: str):
    if "MM" in S or "FF" in S:
        print("No")
    else:
        print("Yes")


solve(N, S)
