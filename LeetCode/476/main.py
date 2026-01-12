class Solution:
    def findComplement(self, num: int) -> int:
        y = list(str(bin(num)).replace("0b", ""))
        for i in range(len(y)):
            if y[i] == "0":
                y[i] = "1"
            else:
                y[i] = "0"
        return int("".join(y), 2)
