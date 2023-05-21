# https://www.hackerrank.com/contests/yfkpo4/challenges/c-012

from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    stra = "".join([str(x) for x in A])

    result0 = N * (N + 1) // 2

    result0 -= stra.count("0")
    for r in stra.split("0"):
        rl = len(r)
        result0 -= rl * (rl + 1) // 2

    result1 = 0
    for r in stra.replace("2", "0").split("0"):
        rl = len(r)
        result1 += rl * (rl - 1) // 2

    result2 = 0
    cs: List[List[int]] = []
    cs.append([A[0], 1])
    for a in A[1:]:
        if a <= 1 and a == cs[-1][0]:
            cs[-1][1] += 1
        else:
            cs.append([a, 1])

    for i in range(len(cs)):
        if cs[i][0] == 2:
            ln1 = cs[i - 1][1] if i - 1 >= 0 and cs[i - 1][0] == 1 else 0
            ln2 = cs[i + 1][1] if i + 1 < len(cs) and cs[i + 1][0] == 1 else 0
            result2 += (ln1 + 1) * (ln2 + 1) - 1

    print(result0, result1, result2)


solve(N, A)
