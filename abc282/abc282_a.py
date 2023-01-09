# https://atcoder.jp/contests/abc282/tasks/abc282_a

N = int(input())


def solve(N: int):
    cs = [chr(ord("A") + x) for x in range(N)]
    print(*cs, sep="")


solve(N)
