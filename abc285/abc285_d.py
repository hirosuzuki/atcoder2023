# https://atcoder.jp/contests/abc285/tasks/abc285_d

from typing import List, Set

N = int(input())
ST = [[x for x in input().split()] for _ in range(N)]


def solve(N: int, ST: List[List[str]]):
    def check() -> bool:
        vs = dict(ST)
        cs: Set[str] = set(s for s, _ in ST)

        while cs:
            us: Set[str] = set()
            s = cs.pop()
            while True:
                if s in us:
                    # print("x", us)
                    return False
                us.add(s)
                if s not in vs:
                    # print("*", us)
                    break
                s = vs[s]
            for s in us:
                if s in cs:
                    cs.remove(s)

        return True

    print(["No", "Yes"][check()])


solve(N, ST)
