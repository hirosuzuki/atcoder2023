# https://atcoder.jp/contests/abc283/tasks/abc283_c

S = input()

def solve(S: str):
    result = 0
    while S:
        if S[0:2] == "00":
            S = S[2:]
            result += 1
        else:
            S = S[1:]
            result += 1
    print(result)

solve(S)
