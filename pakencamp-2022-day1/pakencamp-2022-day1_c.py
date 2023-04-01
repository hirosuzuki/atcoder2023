# https://atcoder.jp/contests/pakencamp-2022-day1/tasks/pakencamp_2022_day1_c

S = input()


def solve(S: str):
    MOD = 998244353
    result = 1
    if len(S) % 2 == 1:
        if S[len(S) // 2] == "?":
            result = 26
    for i in range(len(S) // 2):
        c1 = S[i]
        c2 = S[-i - 1]
        if c1 == "?":
            if c2 == "?":
                result = result * 26 % MOD
        else:
            if c2 != "?" and c1 != c2:
                print(0)
                return
    print(result)


solve(S)
