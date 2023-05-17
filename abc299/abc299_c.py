# https://atcoder.jp/contests/abc299/tasks/abc299_c

N = int(input())
S = input()


def solve(N: int, S: str):
    def calc(S: str) -> int:
        if "o" not in S or "-" not in S:
            return -1
        return max([len(r) for r in S.split("-")])

    print(calc(S))


solve(N, S)
