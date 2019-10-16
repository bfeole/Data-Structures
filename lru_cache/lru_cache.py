from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of:
    - the max number of nodes it can hold,
    - the current number of nodes it is holding,
    - a doubly-linked list that holds the key-value entries in the correct order,
    - a storage dict that provides fast access to every node stored in the cache.
    """

    def __init__(self, limit=10):
        # self.s = {}
        self.limit = limit
        self.order = DoublyLinkedList()
        self.storage = dict()
        self.size = 0

    """
    Retrieves the value associated with the given key. 

    # what is determing if it is most-recently used? The index/order of our dll?

    Also needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.

    Returns the value associated with the key 
    or
    None if the key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if we have a key in our new dict
        if key in self.storage:
            # get the value /node? associated with that key
            get_node = self.storage[key]
            # pass in that node to our dll function move_to_end
            self.order.move_to_end(get_node)
            # return the node of that key
            return get_node

    """
    Adds the given key-value pair to the cache. 
    
    The newly-added pair should be considered the most-recently used
    entry in the cache. 
    
    If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. 
    
    Additionally, in the case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if len(self.order) >= len(self.storage):
