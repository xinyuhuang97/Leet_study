class RandomizedSet:

    def __init__(self):
        self.rd_set=dict()

    def insert(self, val: int) -> bool:
        if val not in self.rd_set.keys():
            self.rd_set[val]=1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.rd_set.keys():
            del self.rd_set[val]
            return True
        return False
    

    def getRandom(self) -> int:
        keys=list(self.rd_set.keys())
        nb=len(keys)
        list_rd=list(keys)

        import random
        return keys[random.randint(0, nb-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()