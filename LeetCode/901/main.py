from collections import deque

class StockSpanner:

    def __init__(self):
        self.dq = deque()

    def next(self, price: int) -> int:
        c, temp = 1, 0
        while(self.dq and self.dq[-1][0] <= price) :
            temp = self.dq.pop()
            c += temp[1]
        
        self.dq.append((price, c))

        return self.dq[-1][1]




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)