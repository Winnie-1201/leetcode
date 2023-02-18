class Node:
    def __init__(self, key, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at the right
    def insert(self, node):
        prev = self.right.prev
        prev.next, self.right.prev = node, node
        node.prev, node.next = prev, self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            # needs to update the most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # add the new key value pair to the list and
        # update the cache
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # if reach the cap, remove the LRU and update the most recent
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
