def inlt():
    return (list(map(int, input().split())))


[n, t] = inlt()
s = list(input().strip())

for _ in range(t):
    for i in range(0, n-1, 1):
        if (s[i] == "B" and s[i+1] == "G"):
            s[i], s[i+1] = s[i+1], s[i]

s = "".join(s)

print(s)
