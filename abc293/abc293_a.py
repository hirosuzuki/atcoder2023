# https://atcoder.jp/contests/abc293/tasks/abc293_a

S = input()


def solve(S: str):
    result = "".join(S[i ^ 1] for i in range(len(S)))
    print(result)


solve(S)
