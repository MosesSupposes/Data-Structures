import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(ListNode(value))
        self.size += 1
    def pop(self):
        if (len(self.storage) > 0):
            last_item = self.storage.remove_from_tail()
            self.size -= 1
            if last_item.value is not None:
                return last_item.value
            else:
                return last_item
    
    def len(self):
        return self.size

    def __len__(self):
        return self.size 

print(len(Stack()))