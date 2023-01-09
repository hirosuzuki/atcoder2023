# https://atcoder.jp/contests/abc283/tasks/abc283_c

S = input()


def solve(s: str):
    result = 0
    while s:
        if s[0:2] == "00":
            s = s[2:]
            result += 1
        else:
            s = s[1:]
            result += 1
    print(result)


solve(S)
