# https://atcoder.jp/contests/abc300/tasks/abc300_d

from typing import List

N = int(input())


def solve(N: int):
    M = 10**6
    ps = [True] * (M + 1)
    primes: List[int] = []
    i = 2
    while i <= M:
        if ps[i]:
            primes.append(i)
            j = i
            while j <= M:
                ps[j] = False
                j += i
        i += 1

    # print(len(primes))

    result = 0
    for ai, a in enumerate(primes):
        a2 = a * a
        if a2 > N:
            break
        for ci in range(ai + 2, len(primes)):
            c = primes[ci]
            a2c2 = a2 * c * c
            if a2c2 > N:
                break
            for bi in range(ai + 1, ci):
                b = primes[bi]
                a2bc2 = a2c2 * b
                if a2bc2 > N:
                    break
                # print(a2bc2, a, b, c)
                result += 1

    print(result)


solve(N)
