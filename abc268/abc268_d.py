# https://atcoder.jp/contests/abc268/tasks/abc268_d

from itertools import permutations
from sys import setrecursionlimit
from typing import Iterator, List

setrecursionlimit(300000)

N, M = [int(x) for x in input().split()]
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]


def solve(N: int, M: int, S: List[str], T: List[str]):
    # print(N, M, S, T)

    tlen = sum(len(w) for w in S)
    # print("tlen", tlen)

    ts = set(T)

    def calc(n: int, m: int) -> Iterator[List[int]]:
        # print("calc", n, m)
        if n <= 0:
            yield []
        else:
            for i in range(m + 1):
                for j in calc(n - 1, m - i):
                    yield [i] + j

    cnt = 0
    for n in permutations(S):
        # print("p", n)
        for s in calc(N - 1, 16 - N + 1 - tlen):
            x = n[0]
            for i in range(N - 1):
                x += "_" * (s[i] + 1) + n[i + 1]
            print(n, s, x)
            cnt += 1
            if x not in ts:
                print("***", x)
                # return
                ...

    print(-1)


solve(N, M, S, T)
