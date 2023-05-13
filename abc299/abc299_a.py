# https://atcoder.jp/contests/abc299/tasks/abc299_a

N = int(input())
S = input()


def solve(N: int, S: str):
    _, v, _ = S.split("|")
    if "*" in v:
        print("in")
    else:
        print("out")


solve(N, S)
