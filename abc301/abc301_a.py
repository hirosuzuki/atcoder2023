# https://atcoder.jp/contests/abc301/tasks/abc301_a

N = int(input())
S = input()


def solve(N: int, S: str):
    tc = S.count("T")
    ac = S.count("A")
    if tc == ac:
        tc = S[:-1].count("T")
        ac = S[:-1].count("A")
    if tc > ac:
        print("T")
    else:
        print("A")


solve(N, S)
