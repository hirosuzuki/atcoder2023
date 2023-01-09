# https://atcoder.jp/contests/abc279/tasks/abc279_b

S = input()
T = input()


def solve(S: str, T: str):
    if T in S:
        print("Yes")
    else:
        print("No")


solve(S, T)
