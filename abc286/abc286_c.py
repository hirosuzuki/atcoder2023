# https://atcoder.jp/contests/abc286/tasks/abc286_c

N, A, B = [int(x) for x in input().split()]
S = input()


def solve(N: int, A: int, B: int, S: str):
    def calc(s: str) -> int:
        result = 0
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                result += B
        # print(s, result)
        return result

    s = S
    result = N * B
    for i in range(N // 2):
        result = min(calc(s) + i * A, result)
        s = s[1:] + s[0]
    print(result)


solve(N, A, B, S)
