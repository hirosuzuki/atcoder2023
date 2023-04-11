# https://atcoder.jp/contests/abc297/tasks/abc297_b

S = input()


def solve(S: str):
    def check(S: str) -> bool:
        if (S.index("B") ^ S.rindex("B") & 1) == 0:
            return False
        if S.replace("Q", "").replace("B", "").replace("N", "") != "RKR":
            return False
        return True

    if check(S):
        print("Yes")
    else:
        print("No")


solve(S)
