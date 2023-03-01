# https://atcoder.jp/contests/abc291/tasks/abc291_a

S = input()


def solve(S: str):
    result = 0
    for i, c in enumerate(S):
        if "A" <= c <= "Z":
            result = i + 1
            break
    print(result)


solve(S)
