from doubly_linked_list import DoublyLinkedList

# Helpers

def find_key(value, dict):
    for key, val in dict.items():
        if val == value:
            return key


def remove_key_if_contained(value, _dict):
    key_of_removed_item = find_key(value, _dict) 
    if key_of_removed_item in _dict:
        del _dict[key_of_removed_item]

# ---------------------------------------------------------------------
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
        self.size = 0
        self.cache = DoublyLinkedList()
        self.map = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.map:
            # Move item to the front of the cache 
            self.cache.move_to_front(self.map[key])
            # Return the requested value
            return self.map[key].value
        else:
            return None

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
        # If the key is already in the cache...
        if key in self.map:
            # Overwrite the existing value by moving it to the front
            # of the cache.
            self.cache.move_to_front(self.map[key])

        # If the key isn't already in the cache...
        else:
            # If the cache has reached max capacity 
            if self.size == self.limit:
                # Remove the least recently used value from the cache
                # and the map
                self.cache.remove_from_tail()
                remove_key_if_contained(self.cache.tail.value, self.map)
                # Add the value to the front of the cache 
                self.cache.add_to_head(value) 
                
            # If the cache hasn't reached max capacity
            else:
                # Simply add it to the head of the cache
                # Increment the size of the cache
                self.cache.add_to_head(value) 
                self.size += 1

        # Whether the key already existed in the cache or not...
        # Store a pointer to the newly inserted node into
        # the map for easy retrival in the future
        self.map[key] = self.cache.head



