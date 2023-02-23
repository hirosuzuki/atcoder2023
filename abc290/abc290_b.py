# https://atcoder.jp/contests/abc290/tasks/abc290_b

N, K = [int(x) for x in input().split()]
S = input()


def solve(N: int, K: int, S: str):
    rs = list(S)
    j = K
    for i in range(len(rs)):
        if rs[i] == "o":
            if j <= 0:
                rs[i] = "x"
            else:
                j -= 1
    print(*rs, sep="")


solve(N, K, S)
