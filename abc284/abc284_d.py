# https://atcoder.jp/contests/abc284/tasks/abc284_d

from typing import List, Tuple

T = int(input())
test = [int(input()) for _ in range(T)]


def solve(T: int, ns: List[int]):
    M = 2200000
    cs = [True] * M
    primes: List[int] = []
    for i in range(2, M):
        if cs[i]:
            primes.append(i)
            for j in range(i, M, i):
                cs[j] = False

    def calc(n: int) -> Tuple[int, int]:
        for i in primes:
            if n % i == 0:
                m = n // i
                if m % i == 0:
                    return (i, m // i)
                else:
                    return (int(m ** (1 / 2)), i)
        return -1, -1

    for n in ns:
        print(*calc(n))


solve(T, test)
