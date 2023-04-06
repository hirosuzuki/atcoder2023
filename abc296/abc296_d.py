# https://atcoder.jp/contests/abc296/tasks/abc296_d

from math import ceil, sqrt

N, M = [int(x) for x in input().split()]


def solve(N: int, M: int):
    if N * N < M:
        print(-1)
        return
    result = N * N
    for i in range(1, min(N, ceil(sqrt(M))) + 1):
        j = ceil(M / i)
        if j > N:
            continue
        k = i * j
        # print(i, j, k)
        if k < result:
            result = k
    print(result)


solve(N, M)
