# https://atcoder.jp/contests/abc280/tasks/abc280_d

from typing import List, Tuple

K = int(input())

def solve(K: int):
    M = 10**6
    
    cs: List[bool] = [True] * (M + 1)
    ss: List[int] = []
    i = 2
    while i <= M:
        if cs[i]:
            for n in range(i, M + 1, i):
                cs[n] = False
            ss.append(i)
        i += 1

    rs: List[Tuple[int, int]] = []
    r = K
    for s in ss:
        if r % s == 0:
            n = 0
            while r % s == 0:
                r //= s
                n += 1
            rs.append((s, n))
    if r > 1:
        rs.append((r, 1))

    def calc(r: int, n: int) -> int:
        k = 0
        i = 0
        while k < n:
            i += 1
            m = r * i
            while m % r == 0:
                m //= r
                k += 1

        #print("calc", r, n, i, k)

        return r * i

    result = 1
    for r, n in rs:
        result = max(result, calc(r, n))

    print(result)


solve(K)
