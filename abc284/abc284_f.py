# https://atcoder.jp/contests/abc284/tasks/abc284_f

from typing import List


def z_algorithm(S: str) -> List[int]:
    result: List[int] = [0] * len(S)

    result[0] = len(S)
    i = 1
    j = 0
    while i < len(S):
        while i + j < len(S) and S[j] == S[i + j]:
            j += 1
        result[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < len(S) and k + result[k] < j:
            result[i + k] = result[k]
            k += 1
        i += k
        j -= k

    return result


# print(z_algorithm("aaabaaaab"))

N = int(input())
T = input()


def solve(N: int, T: str):
    a = T[:N]
    b = T[N:][::-1]
    # print(a, b)
    za_x = z_algorithm(a + b) + [0]
    za_y = z_algorithm(b + a) + [0]
    # print(za_x)
    # print(za_y)
    for i in range(N):
        if za_x[2 * N - i] < i:
            continue
        if za_y[N + i] < N - i:
            continue
        print(T[:i] + T[N + i :])
        print(i)
        return
    print(-1)


solve(N, T)
