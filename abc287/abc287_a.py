# https://atcoder.jp/contests/abc287/tasks/abc287_a

N = int(input())
r = 0
for _ in range(N):
    x = input()
    if x == "For":
        r += 1

if r > N // 2:
    print("Yes")
else:
    print("No")
