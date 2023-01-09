# https://atcoder.jp/contests/abc279/tasks/abc279_a

S = input()


def solve(S: str):
    result = 0
    for c in S:
        if c == "v":
            result += 1
        elif c == "w":
            result += 2
    print(result)


solve(S)
