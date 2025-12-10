# Last updated: 10/12/2025, 07:41:15
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0        

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        newNode = Node(val, self.head)
        self.head = newNode
        self.size += 1

    def addAtTail(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
        self.size += 1

    def addAtIndex(self, index, val):
        # invalid index
        if index < 0 or index > self.size:
            return
        
        # insert at head
        if index == 0:
            self.addAtHead(val)
            return
        
        curr = self.head
        for _ in range(index - 1):    
            curr = curr.next
        
        newNode = Node(val, curr.next)
        curr.next = newNode
        self.size += 1

    def deleteAtIndex(self, index):
        # invalid
        if index < 0 or index >= self.size:
            return

        # delete head
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        curr = self.head
        for _ in range(index - 1):          
            curr = curr.next
        
        curr.next = curr.next.next
        self.size -= 1
