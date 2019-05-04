class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.isEmpty():
            raise RuntimeError ("Attempt to pop and empty stack")
        topIdx = len(self.items)-1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item
    
    def top(self):
        if self.isEmpty():
            raise RuntimeError ("Attempt to get top of empty stack")
        topIdx = len (self.items)-1
        return self.items[topIdx]
    
    def push(self, item):
        self.items.append(item)
    
    def isEmpty(self):
        return len(self.items) == 0

def main():
    s = Stack()
    
    '''
    lst = list (range(10))
    lst = []  
    for k in lst:
        s.push(k)
    if s.top() == 9:
        print ("test 1 passed")
    else:
        print ("test 1 failed")
    ''' 
    s.push(55)

    print ("Get the top: ", s.top())


if __name__ == "__main__":
    main()