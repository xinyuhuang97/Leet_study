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
        if key in self.m:
            node=self.m[key]
            ans=node.value
            del self.m[key]
            self.del_node(node)
            self.add_node(node)
            self.m[key]=self.head.next
            return ans
        return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.m.keys():
            cur=self.m[key]
            del self.m[key]
            self.del_node(cur)
        if self.capacity==len(self.m):
            del self.m[self.tail.prev.key]
            self.del_node(self.tail.prev) 
        self.add_node(self.Node(key, value))
        self.m[key]=self.head.next
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)