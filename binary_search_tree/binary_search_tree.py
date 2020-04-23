import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
from queue import Queue

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            # Base case
            else:
                self.left = BinarySearchTree(value)
        # If value is greater than or equal to self.value...
        else:
            if self.right is not None:
                self.right.insert(value)
            # Base case
            else:
                self.right = BinarySearchTree(value) 
  
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base case
        if target == self.value:
            return True
        
        if target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            # Base case
            else:
                return False
        if target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            # Base case
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        def determine_max(prev_max, tree):
            if tree.value >= prev_max:
                if tree.right is not None:
                    return determine_max(prev_max, tree.right)
                else:
                    prev_max = tree.value
                    return prev_max
            
            # If tree.value is less than the prev max... 
            else:
                return prev_max

        return determine_max(self.value, self)

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left is not None:
            self.left.for_each(cb)

        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        _list = []
        def keep_track(node):
            if node is None:
                return
            else:
                _list.append(node.value)
                keep_track(node.left)
                keep_track(node.right)

        keep_track(self)
        _list.sort()

        for item in _list:
            print(item)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.put(node)

        while not q.empty():
            _node = q.get()
            print(_node.value)

            if _node.left is not None:
                q.put(_node.left)
            
            if _node.right is not None:
                q.put(_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)
        
        if self.left is not None:
            self.left.dft_print(node.left)

        if self.right is not None:
            self.right.dft_print(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
