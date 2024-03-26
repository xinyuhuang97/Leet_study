import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=collections.deque([])
        self.value_key={}
    def get(self, key: int) -> int:
        #print(key,self.cache)
        if key in self.value_key.keys():
            self.cache.remove(key)
            self.cache.append(key)
            return self.value_key[key]
        return -1

    def put(self, key: int, value: int) -> None:
        #print(key, value)
        #print(self.cache)
        if key in self.value_key.keys():
            self.cache.remove(key)
            self.cache.append(key)
            self.value_key[key]=value
        else:
            if self.capacity==len(self.cache):
                delete_cache=self.cache.popleft()
                self.value_key.pop(delete_cache,None)
                #print(self.cache)
            self.cache.append(key)
            self.value_key[key]=value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)