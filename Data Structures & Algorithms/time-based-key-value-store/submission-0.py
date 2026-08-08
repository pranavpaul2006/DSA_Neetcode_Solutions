class TimeMap:

    def __init__(self):
        self.kv_pair = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv_pair:
            self.kv_pair[key] = []
        self.kv_pair[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.kv_pair.get(key,[])

        l,r = 0 , len(values) - 1
        while l <= r:
            m = (l+r) // 2
            if (values[m][1]) == timestamp:
                res = values[m][0]
                return res
            elif (values[m][1]) < timestamp:
                l = m+1
                res = values[m][0]
            else:
                r = m - 1

        return res

            