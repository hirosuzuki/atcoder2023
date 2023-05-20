# https://www.hackerrank.com/contests/yfkpo4/challenges/yurufuwa-string-1

S = input()


def check(S: str) -> bool:
    if S[1] == S[3] == S[5] == "u" and S[7] == "a":
        return True
    return False


if check(S):
    print("Yes")
else:
    print("No")
