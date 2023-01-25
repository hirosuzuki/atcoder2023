# https://atcoder.jp/contests/abc273/tasks/abc273_a

N = int(input())


def solve(N: int):
    def f(x: int) -> int:
        if x < 0:
            raise
        if x == 0:
            return 1
        return x * f(x - 1)

    print(f(N))


solve(N)
