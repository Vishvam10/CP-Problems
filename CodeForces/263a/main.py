def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


n = 5
mat = []
posx = 0
posy = 0
for _ in range(n):
    mat.append(inlt())

for x in range(n):
    for y in range(n):
        if mat[x][y] == 1:
            posx = x
            posy = y
            break

print(abs(2 - posx) + abs(2 - posy))
