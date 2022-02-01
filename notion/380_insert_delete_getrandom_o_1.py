import random

class RandomizedSet:

    def __init__(self):
        self.seen = set()
        self.arr = [] 

    def insert(self, val: int) -> bool:
        if val not in self.seen:
            self.seen.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.seen:
            self.seen.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        ret_idx = random.randint(0, len(self.seen) - 1)
        idx = 0
        for x in self.seen:
            if ret_idx == idx:
                return x 



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
