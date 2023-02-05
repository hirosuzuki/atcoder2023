# https://atcoder.jp/contests/abc270/tasks/abc270_e

from collections import Counter
from typing import List

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, K: int, A: List[int]):
    cs = Counter(A)
    vs = sorted(cs)
    m = N
    p = 0
    left = K
    for v in vs:
        h = v - p
        if left <= m * h:
            # print(v, p, h, m, left)
            d, dm = divmod(left, m)
            y = p + d
            left -= d * m
            # print("*", y, left)
            result: List[int] = []
            for x in A:
                xx = min(x, y)
                if dm > 0 and x > xx:
                    dm -= 1
                    xx += 1
                result.append(x - xx)
            print(*result)
            break
        else:
            left -= m * h
        # print(v, p, h, m, left)
        #
        m -= cs[v]
        p = v


solve(N, K, A)
