#https://www.tutorialspoint.com/python/python_advanced_linked_list.htm

class LinkedList:
    class __Node:
            def __init__(self, item, next=None):
                self.item = item
                self.next = next
              
            def getItem(self):
                return self.item

            def getNext(self):
                return self.next

            def setItem(self, item):
                self.item = item
            
            def setNext (self, next):
                self.next = next
    
    def __init__(self, contents = []):
        self.first = LinkedList.__Node (None, None)
        self.last = self.first
        self.numItems = 0 