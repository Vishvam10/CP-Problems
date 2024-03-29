import copy


def inlt():
    return (list(map(int, input().split())))


n = int(input())
arr = inlt()
k = int(input())
direction = 'l'

cpy = copy.deepcopy(arr)
if (direction == 'l'):
    for i in range(n):
        arr[(i-k) % n] = cpy[i]
elif (direction == 'r'):
    for i in range(n):
        arr[(i+k) % n] = cpy[i]

for x in arr:
    print(x, end=' ')
