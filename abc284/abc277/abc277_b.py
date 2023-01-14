# https://atcoder.jp/contests/abc277/tasks/abc277_b

from typing import List, Set

N = int(input())
S = [input() for _ in range(N)]


def solve(N: int, S: List[str]):
    def check(S: List[str]) -> bool:
        cs: Set[str] = set()
        for r in S:
            if r[0] not in "HDCS":
                return False
            if r[1] not in "A23456789TJQK":
                return False
            if r in cs:
                return False
            cs.add(r)
        return True

    print(["No", "Yes"][check(S)])


solve(N, S)
