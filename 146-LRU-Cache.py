class Node:
    def __init__(self, k, v, n=None, p=None):
        self.key, self.value = k, v
        self.next, self.prev = n, p
    
class LRUCache:

    def __init__(self, capacity: int):
        self.n, self.hmap = capacity, {}
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def insert(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next, node.next.prev = node, node
        
    def delete(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        
    def get(self, key: int) -> int:
        if key not in self.hmap: return -1
        node = self.hmap[key]
        self.delete(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.delete(self.hmap.pop(key))
        if len(self.hmap) == self.n:
            self.delete(self.hmap.pop(self.tail.prev.key))
        node = self.hmap[key] = Node(key, value)
        self.insert(node)
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
