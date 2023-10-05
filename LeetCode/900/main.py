"""
DIFFICULTY : medium
TAGS : array, design, counting, iterator
"""
class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.ptr = 0
        self.arr = encoding
        
    def next(self, n: int) -> int:
        while(n > 0 and self.ptr < len(self.arr)) :
            if(n > self.arr[self.ptr]) :
                n -= self.arr[self.ptr]
                self.ptr += 2
            else :
                # Decrease the element frequence
                self.arr[self.ptr] -= n
                return self.arr[self.ptr + 1]
        return -1
                
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)