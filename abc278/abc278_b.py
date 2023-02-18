# https://atcoder.jp/contests/abc278/tasks/abc278_b

H, M = [int(x) for x in input().split()]


def solve(H: int, M: int):
    def check(H: int, M: int) -> bool:
        return 0 <= H <= 23 and 0 <= M <= 59

    h, m = H, M
    while True:
        if check(h // 10 * 10 + m // 10, m // 10 + h % 10 * 10):
            break
        m += 1
        if m >= 60:
            m = 0
            h = (h + 1) % 24
    print(h, m)


solve(H, M)
