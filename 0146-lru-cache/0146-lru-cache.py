import collections
class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.prev=None
            self.next=None
            self.key=key
            self.value=value
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=self.Node(-1,-1)
        self.tail=self.Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.m={}
    def add_node(self, node):
        tmp=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=tmp
        tmp.prev=node
        
    def del_node(self, node):
        node.next.prev=node.prev
        node.prev.next=node.next
        
        
    def get(self, key: int) -> int:
        if key in self.m.keys():
            ans=self.m[key].value
            node=self.m[key]
            del self.m[key]
            self.del_node(node)
            self.add_node(node)
            self.m[key]=self.head.next
            return ans
        return -1
            
    def put(self, key: int, value: int) -> None:
        head=self.head
        while head!=None:
            head=head.next
        if key in self.m.keys():
            cur=self.m[key]
            del self.m[key]
            self.del_node(cur)
        if self.capacity==len(self.m):
            del self.m[self.tail.prev.key]
            self.del_node(self.tail.prev)
            
        self.add_node(self.Node(key, value))
        self.m[key]=self.head.next
            
        
"""
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
            
"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)