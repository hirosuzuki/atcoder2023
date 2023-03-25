# https://atcoder.jp/contests/abc294/tasks/abc294_b


from typing import List

H, W = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(H)]


def solve(H: int, W: int, A: List[List[int]]):
    for r in A:
        print("".join(chr(64 + n if n >= 1 else ord(".")) for n in r))


solve(H, W, A)
