# https://atcoder.jp/contests/abc283/tasks/abc283_d

from typing import Set

S = input()

def solve(S: str):

    def check(S: str) -> bool:
        css: List[Set[str]] = [set()]
        tcs: Set(str) = set()
        for i, c in enumerate(S):
            if c == "(":
                css.append(set())
            elif c == ")":
                tcs = tcs - css.pop()
            else:
                if c in tcs:
                    return False
                tcs.add(c)
                css[-1].add(c)
        return True

    if check(S):
        print("Yes")
    else:
        print("No")

solve(S)
