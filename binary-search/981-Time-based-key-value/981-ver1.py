class TimeMap:

    def __init__(self):
        self.time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.time:
            self.time[key] = []

        self.time[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if not key in self.time:
            return ""

        if timestamp < self.time[key][0][0]:
            return ""

        left, right = 0, len(self.time[key])

        while left < right:
            mid = (left + right) // 2

            if self.time[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return "" if right == 0 else self.time[key][right - 1][1]

        # for curr in reversed(range(1, timestamp + 1)):
        #     if curr in self.time[key]:
        #         return self.time[key][curr]
        # return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
