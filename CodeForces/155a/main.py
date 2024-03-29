def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    return (input().strip())


n = inp()
arr = inlt()
max_till_now = [arr[0]]
min_till_now = [arr[0]]
ans = 0

for i in range(1, n):
    if (arr[i] > max_till_now[-1]):
        ans += 1
        max_till_now.append(arr[i])
    elif (arr[i] < min_till_now[-1]):
        ans += 1
        min_till_now.append(arr[i])

print(ans)
