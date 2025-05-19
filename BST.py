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
                self.left.parent = self 
            else:
                self.left.insertRequest(id, name)
        else:
            if self.right is None:
                self.right = BST(id, name)
                self.right.parent = self 
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
                print(f"\n{id} do not exists.\n")
                return None
            else:
                return self.left.searchRequest(id)
        elif id > self.ID:
            if self.right is None:
                print(f"\n[search] ID:{id} do not exists.\n")
                return None
            else:
                return self.right.searchRequest(id)
        else:
            print(f"\n[search] ID: {id}, name: {self.Name} found.\n")
            return self
                
    
    def deleteRequest(self, id):
        node = self.searchRequest(id)
        if node != None:
            return self.delete_node(node)
    def delete_node(self, node):

        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
       
        def num_children(n):
            num_children = 0
            if n.left!=None:
                num_children+=1
            if n.right!=None:
                num_children+=1
            return num_children
        
        
        node_parent = node.parent
        
        node_children = num_children(node)

        #CASE1
        if node_children==0:
           
            if node_parent is None:
                self.ID = None
                self.Name = None
            else:
            
                if node_parent.left==node:
                    node_parent.left=None
                else:
                    node_parent.right=None
        
        #case2 
        if node_children==1:
            
            if node.left!=None:
                child=node.left
            else:
                child=node.right 
            
            if node_parent is None:
                
                self.ID = child.ID
                self.Name = child.Name
                self.left = child.left
                self.right = child.right
                if self.left:
                    self.left.parent = self
                if self.right:
                    self.right.parent = self
            else:
           
                if node_parent.left==node:
                    node_parent.left=child
                else:
                    node_parent.right=child

               
                child.parent=node_parent

        #case 3
        if node_children==2:
             
            successor = min_value_node(node.right)
            
            node.ID = successor.ID 
            
            self.delete_node(successor)
    
    def isEmptyBST(self):
        return self is None  

    def sizeBST(self):
        count = 1
        if self.left:
            count += self.left.sizeBST()
        if self.right:
            count += self.right.sizeBST()
        return count
