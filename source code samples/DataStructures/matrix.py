# double list

class Board:
    matrix = []
    quadraticlimit = 0
    
    def __init__(self,board=None, limit = 3):
        self.quadraticlimit = 3
    
    def brutalWay(self):
        for i in range(self.quadraticlimit):
            self.matrix.append([])
            for j in range(self.quadraticlimit):
                self.matrix[i].append(i+j)

    def elegantWay(self):
        elegantMatrix = [[0 for y in range(self.quadraticlimit)] for x in range (self.quadraticlimit)]
        return elegantMatrix

    def print(self):
        for i in range(self.quadraticlimit):
            for j in range(self.quadraticlimit):
                print ("i=", i, "j= ", j ," => ", self.matrix[i][j]) 
            print ("")

if __name__ == "__main__":
    b = Board()
    b.brutalWay()
    b.print()
    print ("======================\n")
    b.elegantWay()
    b.print()

