def insr():
    return (input().strip())


def solve(s):
    print('+'.join(list(sorted(s.replace('+', '')))))
    return


inp = insr()
solve(inp)
