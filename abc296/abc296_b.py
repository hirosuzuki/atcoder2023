# https://atcoder.jp/contests/abc296/tasks/abc296_b

from typing import List

S = [input() for _ in range(8)]


def solve(S: List[str]):
    for y, row in enumerate(S):
        for x, col in enumerate(row):
            if col == "*":
                print("{}{}".format(chr(x + ord("a")), 8 - y))
                return


solve(S)
