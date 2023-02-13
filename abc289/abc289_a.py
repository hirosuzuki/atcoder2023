# https://atcoder.jp/contests/abc289/tasks/abc289_a

S = input()


def solve(S: str):
    result = "".join("10"[c == "1"] for c in S)
    print(result)


solve(S)
