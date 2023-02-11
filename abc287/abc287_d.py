# https://atcoder.jp/contests/abc287/tasks/abc287_d

S = input()
T = input()


def solve(S: str, T: str):
    hn = 0
    tn = 0
    for i in range(len(T)):
        if S[i] != "?" and T[i] != "?" and S[i] != T[i]:
            break
        hn = i + 1
    for i in range(1, len(T) + 1):
        if S[-i] != "?" and T[-i] != "?" and S[-i] != T[-i]:
            break
        tn = i
    # print(hn, tn)
    for i in range(len(T) + 1):
        if i <= hn and len(T) - i <= tn:
            print("Yes")
        else:
            print("No")


solve(S, T)
