# https://atcoder.jp/contests/abc282/tasks/abc282_c

N = int(input())
S = input()

def solve(N: int, S: str):
    result = []
    bc = 0
    for i, c in enumerate(S):
        if c == '"':
            bc += 1
        if c == "," and bc % 2 == 0:
            c = "."
        result.append(c)

    print("".join(result))


solve(N, S)

