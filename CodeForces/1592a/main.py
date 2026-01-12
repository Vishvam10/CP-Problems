from sys import stdin, stdout, setrecursionlimit
from io import BytesIO, IOBase

setrecursionlimit(10000)


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        import os

        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
        self.BUFSIZE = 8192

    def read(self):
        while True:
            a = self.os.read(
                self._fd, max(self.os.fstat(self._fd).st_size, self.BUFSIZE)
            )
            if not a:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(a), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            a = self.os.read(
                self._fd, max(self.os.fstat(self._fd).st_size, self.BUFSIZE)
            )
            self.newlines = a.count(b"\n") + (not a)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(a), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


stdin, stdout = IOWrapper(stdin), IOWrapper(stdout)


def input():
    return stdin.readline().rstrip("\r\n")


# inf = float('inf')
# ninf = float('-inf')
# abc = 'abcdefghijklmnopqrstuvwxyz'


def inp():
    return int(input())


# st = lambda: input().strip()
# jn = lambda x,l: x.join(map(str,l))


def int_arr():
    return list(map(int, input().strip().split()))


# str_arr = lambda :list(map(str,input().split()))
# get_str = lambda : map(str,input().strip().split())
def get_int():
    return map(int, input().strip().split())


# get_float = lambda : map(float,input().strip().split())


mod = 1000000007

for _ in range(inp()):
    n, H = get_int()
    a = int_arr()
    a.sort()
    x = a[-1]
    y = a[-2]
    if H % (x + y) == 0:
        print(2 * (H // (x + y)))
    elif H % (x + y) <= x:
        print(2 * (H // (x + y)) + 1)
    else:
        print(2 * (H // (x + y)) + 2)
