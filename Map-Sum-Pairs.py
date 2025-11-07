class MapSum:

    def __init__(self):
        self.store = {}

    def insert(self, key: str, val: int) -> None:
        self.store[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        for k, v in self.store.items():
            if k.startswith(prefix):
                total += v
        return total



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)