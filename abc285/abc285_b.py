# https://atcoder.jp/contests/abc285/tasks/abc285_b

N = int(input())
S = input()


def solve(N: int, S: str):
    def check(i: int) -> int:
        result = 0
        j = 0
        while j + i < len(S):
            if S[j + i] == S[j]:
                break
            result += 1
            j += 1
        return result

    for i in range(1, N):
        print(check(i))


solve(N, S)
