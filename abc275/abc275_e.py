# https://atcoder.jp/contests/abc275/tasks/abc275_e

N, M, K = [int(x) for x in input().split()]


def solve(N: int, M: int, K: int):
    cs = [1] + [0] * N
    for _ in range(K):
        ncs = [0] * N + [cs[N] * M]
        for i in range(1, M + 1):
            for j in range(N):
                k = j + i
                if k > N:
                    k = N - (k - N)
                ncs[k] += cs[j]
        cs = ncs

    MOD = 998244353
    s = M**K
    r = (pow(s, -1, MOD) * cs[-1]) % MOD
    print(r)


solve(N, M, K)
