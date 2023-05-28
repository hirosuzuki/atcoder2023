# https://atcoder.jp/contests/abc301/tasks/abc301_c

from collections import defaultdict
from typing import DefaultDict

S = input()
T = input()


def solve(S: str, T: str):
    def check(s: str, t: str) -> bool:
        sc: DefaultDict[str, int] = defaultdict(int)
        tatc = 0
        for c in S:
            sc[c] += 1
        for c in T:
            if c == "@":
                tatc += 1
            elif sc[c] > 0:
                sc[c] -= 1
            elif c in "atcoder" and sc["@"] > 0:
                sc["@"] -= 1
            else:
                return False

        for c in sc:
            if sc[c] > 0:
                if c in "@atcoder" and tatc > 0:
                    tatc -= 1
                else:
                    return False

        return True

    if check(S, T):
        print("Yes")
    else:
        print("No")


solve(S, T)
