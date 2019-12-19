import sys
sys.path.append('../doubly_linked_list/')
from doubly_linked_list import DoublyLinkedList

# FIFO First in First Out
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size +=1


    def dequeue(self):
        while self.storage.head is not None:
            self.size -=1
            self.storage.remove_from_head()
            return
            

    def len(self):
        return self.size
