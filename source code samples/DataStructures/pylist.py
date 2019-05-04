#Costumize a list in python

class PyList:
    def __init__(self, contents=[], size=10):
        self.items = [None]*size
        self.numItems = size
        self.size = size

        for e in contents:
            print ("Append = ", e)
            self.items.append(e)

    def print(self):
        for i in self.items:
            print(i)
    
    def printVersion2(self):
        idx = 0
        while idx < self.size-1:
            print ("value: ", self.items[idx], " at position :", idx)
            idx = idx + 1
        print()

    def __getitem__(self, index):
        if index >=0 and index < len(self.items):
            return self.items[index]
        raise IndexError ("PyList index out of range")
    
    def __setitem__(self, index,val):
        if index >=0 and index < len(self.items):
            self.items[index] = val
            return
        raise IndexError ("PyList index out of range")

    def __makeroom(self):
        newlen = (self.size // 4) + self.size + 1
        newlst = [None]  * newlen
        for i in range(self.numItems):
            newlst[i] = self.items[i]
        self.items = newlst
        self.size = newlen
    
    def append(self,item):
        if self.numItems == self.size:
            self.__makeroom()
        self.items[self.numItems] = item
        self.numItems +=1
    
    def __add_(self, other):
        result = PyList(size=self.numItems+other.numItems)
        for i in range(self.numItems):
            result.append(self.items[i])
        for i in range(other.numItems):
            result.append(self.items[i])
        return result 

    def __len__(self):
        return len(self.items)

if __name__ == "__main__":
    sample = PyList(["a", "b", "c"])
    sample.print()
    sample.printVersion2()
    #print ("Index value at 8 position: ", sample.__getitem__(11))
    sample.__setitem__(1, "w")
    sample.printVersion2()
    sample.append(["n","o"])
    sample.printVersion2()
    print ("Size of List: ",sample.__len__())