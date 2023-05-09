# https://atcoder.jp/contests/abc298/tasks/abc298_d

from collections import deque
from typing import List

Q = int(input())
query = [[int(x) for x in input().split()] for _ in range(Q)]


def solve(Q: int, query: List[List[int]]):
    M = 998244353
    result = 1
    q = deque([1])

    for qry in query:
        if qry[0] == 1:
            x = qry[1]
            q.append(x)
            result = (result * 10 + x) % M
        elif qry[0] == 2:
            x = q.popleft()
            n = len(q)
            r = x * pow(10, n, M)
            result = (result - r) % M
        elif qry[0] == 3:
            print(result)


solve(Q, query)
