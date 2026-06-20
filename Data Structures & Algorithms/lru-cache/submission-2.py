from collections import defaultdict

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.left = self.right = None
        self.num = 0
    
    def remove(self, node):
        if node is None:
            return
        if node.prev is None:
            self.left = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.right = node.prev
        else:
            node.next.prev = node.prev
        self.dic[node.key] = None
        self.num -= 1
        del node
    
    def insert(self, node):
        if node is None:
            return
        self.num += 1
        if self.right is None:
            self.left = self.right = node
        else:
            self.right.next = node
            node.prev = self.right
            self.right = node

    def get(self, key: int) -> int:
        if self.dic.get(key, None) is not None:
            value = self.dic[key].value
            self.remove(self.dic[key])
            node = Node(key, value)
            self.insert(node)
            self.dic[key] = node
            return value
        return -1
        
    def put(self, key: int, value: int) -> None:
        
        self.remove(self.dic.get(key, None))
        self.dic[key] = Node(key, value)
        self.insert(self.dic[key])
        
        if self.num > self.capacity:
            self.remove(self.left)
        

        
