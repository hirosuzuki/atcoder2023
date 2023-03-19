# https://atcoder.jp/contests/abc268/tasks/abc268_a

S = input()
T = input()


def solve(S: str, T: str):
    if T[: len(S)] == S:
        print("Yes")
    else:
        print("No")


solve(S, T)
