# https://atcoder.jp/contests/abc298/tasks/abc298_a

N = int(input())
S = input()


def solve(N: int, S: str):
    def check(S: str) -> bool:
        if "x" in S:
            return False
        if "o" in S:
            return True
        return False

    if check(S):
        print("Yes")
    else:
        print("No")


solve(N, S)
