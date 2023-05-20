# https://www.hackerrank.com/contests/yfkpo4/challenges/b-super-miraina-tower

N = int(input())


def calc(N: int) -> int:
    a = 0
    b = 1
    x = 0
    s = 1
    while True:
        if b <= N <= a + b:
            return x + (N - b) * s
        a, b, x, s = b, a + b, x + a * s, -s


print(calc(N))
