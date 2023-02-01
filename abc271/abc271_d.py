# https://atcoder.jp/contests/abc271/tasks/abc271_d

from collections import defaultdict
from typing import DefaultDict, List

N, S = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, S: int, AB: List[List[int]]):
    rs: DefaultDict[int, str] = defaultdict(str)
    rs[0] = ""
    for a, b in AB:
        nrs: DefaultDict[int, str] = defaultdict(str)
        for k in list(rs.keys()):
            nrs[k + a] = rs[k] + "H"
            nrs[k + b] = rs[k] + "T"
        rs = nrs

    if S in rs:
        print("Yes")
        print(rs[S])
    else:
        print("No")


solve(N, S, AB)
