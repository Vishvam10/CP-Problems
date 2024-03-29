class LFUCache:

    def __init__(self, capacity: int):
        self.mp = {}  
        self.counts = defaultdict(list) 
        self.cap = capacity 

    def get(self, key: int) -> int:
        if key in self.mp:
            value, freq = self.mp[key]
            self.counts[freq].remove(key)
            # to avoid pop from empty list
            if not self.counts[freq]:
                del self.counts[freq]
            freq += 1
            self.counts[freq].append(key)
            self.mp[key] = (value, freq)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return

        if key in self.mp:
            self.mp[key] = (value, self.mp[key][1])

            # Update frequency
            self.get(key)
        else:
            if len(self.mp) >= self.cap:
                min_freq = min(self.counts)
                lfu_key = self.counts[min_freq].pop(0)
                del self.mp[lfu_key]
                # to avoid pop from empty list
                if not self.counts[min_freq]:
                    del self.counts[min_freq]

            self.mp[key] = (value, 1)
            self.counts[1].append(key)

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)