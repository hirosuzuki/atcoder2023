# https://atcoder.jp/contests/abc280/tasks/abc280_c

S = input()
T = input()

def solve(S: str, T: str):
    result = 1
    for s, t in zip(S, T):
        if s != t:
            break
        result += 1
    print(result)

solve(S, T)
