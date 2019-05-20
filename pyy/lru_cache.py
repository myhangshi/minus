class Node(object):
    
    def __init__(self, key, val): 
        self.key = key 
        self.val = val 
        self.prev = None
        self.next = None 
        
class DoubleLList(object): 
    
    def __init__(self): 
        self.head = Node(None, 'head')
        self.tail = Node(None, 'tail')
    
        self.head.next = self.tail 
        self.head.prev = None
        self.tail.prev = self.head
        self.tail.next = None 
    
    def get_head(self): 
        return self.head.next
    
    def get_tail(self): 
        return self.tail.prev 
    
    def add(self, node): 
        prev = self.tail.prev 
        prev.next = node 
        node.prev = prev
        node.next = self.tail 
        self.tail.prev = node 
    
    def remove(self, node): 
        prev = node.prev 
        nxt = node.next 
        prev.next = nxt
        nxt.prev = prev 
        


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity 
        self.dict = {}
        self.list = DoubleLList() 
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict: 
            node = self.dict[key]
            
            self.list.remove(node)
            self.list.add(node)
            return node.val 
        
        return -1 
    
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.dict: 
            self.list.remove(self.dict[key])
            del self.dict[key]
        
        node = Node(key, value)
        self.list.add(node)
        self.dict[key] = node 
        
        if len(self.dict) > self.capacity: 
            head = self.list.get_head() 
            self.list.remove(head)
            del self.dict[head.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

