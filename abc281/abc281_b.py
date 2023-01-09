# https://atcoder.jp/contests/abc281/tasks/abc281_b

S = input()


def solve(S: str):
    def check(S: str):
        if len(S) != 8:
            return False
        if not ("A" <= S[0] <= "Z"):
            return False
        if not ("A" <= S[-1] <= "Z"):
            return False

        try:
            n = int(S[1:-1])
        except Exception:
            return False

        if not (100000 <= n <= 999999):
            return False

        return True

    print(["No", "Yes"][check(S)])


solve(S)
