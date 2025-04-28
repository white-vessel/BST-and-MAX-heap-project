class BST:

    def __init__(self, ID, Name):
        self.left = None
        self.right = None
        self.parent = None
        self.ID = ID
        self.Name = Name
    
    def insertRequest(self, id, name):
        if id < self.ID:
            if self.left is None:
                self.left = BST(id, name)
                self.left.parent = self #set parent
            else:
                self.left.insertRequest(id, name)
        else:
            if self.right is None:
                self.right = BST(id, name)
                self.right.parent = self #set parent
            else:
                self.right.insertRequest(id, name)
    
    def printBST(self):
        print(f"ID: {self.ID}, Name: {self.Name}")
        if self.left:
            self.left.printBST()
        if self.right:
            self.right.printBST()

    def searchRequest(self, id):
        if id < self.ID:
            if self.left is None:
                print(f"{id} do not exists.")
            else:
                return self.left.searchRequest(id)
        elif id > self.ID:
            if self.right is None:
                print(f"{id} do not exists.")
            else:
                return self.right.searchRequest(id)
        else:
            print(f"found.\n ID: {id}, name: {self.Name}")
                







# tree = BST(10,'a')
# tree.insertRequest(5,'b')
# tree.insertRequest(4,'c')
# tree.insertRequest(2,'d')
# tree.insertRequest(1,'e')
# tree.insertRequest(3,'f')
# tree.insertRequest(22,'g')
# tree.insertRequest(11,'h')
# tree.insertRequest(12,'i')

# tree.searchRequest(22)
# tree.searchRequest(1)
# tree.searchRequest(6)


