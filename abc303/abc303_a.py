# https://atcoder.jp/contests/abc303/tasks/abc303_a

N = int(input())
S = input()
T = input()


def solve(N: int, S: str, T: str):
    def checkChar(c1: str, c2: str) -> bool:
        return (c1 == c2) or ((c1 + c2) in ("1l", "l1", "0o", "o0"))

    def check(S: str, T: str) -> bool:
        return all(checkChar(c1, c2) for c1, c2 in zip(S, T))

    print(check(S, T) and "Yes" or "No")


solve(N, S, T)
