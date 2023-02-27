# https://atcoder.jp/contests/abc269/tasks/abc269_c

N = int(input())


def solve(N: int):
    ns = bin(N)[2:]

    def printbin(prefix: str, s: str):
        if s:
            printbin(prefix + "0", s[1:])
            if s[0] == "1":
                printbin(prefix + "1", s[1:])
        else:
            print(int(prefix, 2))

    printbin("", ns)


solve(N)
