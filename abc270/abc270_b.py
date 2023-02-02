# https://atcoder.jp/contests/abc270/tasks/abc270_b

X, Y, Z = [int(x) for x in input().split()]


def solve(X: int, Y: int, Z: int):
    x, y, z = X, Y, Z
    if x < 0:
        x, y, z = -x, -y, -z
    if 0 < y < x:
        if 0 < z < y:
            print(x)
            return
        if z < 0:
            print(x - z - z)
            return
        print(-1)
        return
    print(x)
    return


solve(X, Y, Z)
