# https://atcoder.jp/contests/abc276/tasks/abc276_a

S = input()


def solve(S: str):
    if "a" in S:
        r = S.rindex("a")
        print(r + 1)
    else:
        print(-1)


solve(S)
