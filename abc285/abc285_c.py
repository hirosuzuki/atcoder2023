# https://atcoder.jp/contests/abc285/tasks/abc285_c

S = input()


def solve(S: str):
    result = 0
    for i in range(len(S)):
        result += 26**i
    for i in range(len(S)):
        result += (ord(S[-i - 1]) - ord("A")) * (26**i)

    print(result)


solve(S)
