class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append([value, timestamp])         
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.hmap[key]
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            m = (l+r)//2
            if values[m][1] < timestamp:
                l = m + 1
                res = values[m][0]
            elif values[m][1] > timestamp:
                r = m - 1
            else:
                return values[m][0]
        return res
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
