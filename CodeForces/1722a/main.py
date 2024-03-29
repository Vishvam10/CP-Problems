def solve():
    n = int(input())
    s = "".join(sorted(input()))
    print("YES" if s == "Timru" else "NO")


t = int(input())

for i in range(t):
    solve()
