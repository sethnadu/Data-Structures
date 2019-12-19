from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.cache = {}
        self.storage = DoublyLinkedList()
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.cache:
            return None
        elif key in self.cache:
            self.storage.move_to_end(self.cache[key])
            return self.cache[key].value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        print("key :", key)
        print("value :", value)
        if key in self.cache:
            self.cache[key] = ListNode(value, key)
            self.storage.move_to_end(self.cache[key])

        elif key not in self.cache:
            self.cache.update({key:ListNode(value, key)})
            self.storage.add_to_tail(self.cache[key])
            
            if self.storage.length > self.limit:
                key_delete = self.storage.remove_from_head()
                # print("key delete:", key_delete)
                del self.cache[key_delete]
                
                


# cache = LRUCache()
# cache.set('item1', 'a')
# cache.set('item2', 'b')

# cache.set('item3', 'c')

# cache.set('item4', 'z')
