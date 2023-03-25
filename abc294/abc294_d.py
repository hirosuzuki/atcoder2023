# https://atcoder.jp/contests/abc294/tasks/abc294_d


from typing import List

N, Q = [int(x) for x in input().split()]
Events = [[int(x) for x in input().split()] for _ in range(Q)]


def solve(N: int, Q: int, Events: List[List[int]]):
    cs: List[int] = [0] * (N + 1)
    cp = 1
    crp = 1
    for e in Events:
        if e[0] == 1:
            while cs[cp] != 0:
                cp += 1
            cs[cp] = 1
        elif e[0] == 2:
            cs[e[1]] = 2
        elif e[0] == 3:
            while cs[crp] == 2:
                crp += 1
            print(crp)


solve(N, Q, Events)
