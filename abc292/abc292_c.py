# https://atcoder.jp/contests/abc292/tasks/abc292_c

from typing import List

N = int(input())


def solve(N: int):
    cs: List[int] = [0] * (N + 1)
    for i in range(1, N):
        x = i * i
        if x > N:
            break
        cs[x] += 1
        for j in range(i + 1, N):
            x = i * j
            if x > N:
                break
            cs[x] += 2

    result = 0
    for i in range(1, N):
        j = N - i
        result += cs[i] * cs[j]

    print(result)


solve(N)
