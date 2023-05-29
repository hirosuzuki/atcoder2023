# https://atcoder.jp/contests/abc301/tasks/abc301_d

S = input()
N = int(input())


def solve(S: str, N: int):
    result = int(S.replace("?", "0"), 2)
    for i in range(len(S)):
        if S[i] == "?":
            k = 1 << (len(S) - i - 1)
            if result + k <= N:
                result += k
    if result > N:
        result = -1
    print(result)


solve(S, N)
