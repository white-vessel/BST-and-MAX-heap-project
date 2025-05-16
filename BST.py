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
        # return the number of children for the input
        def num_children(n):
            num_children = 0
            if n.left!=None:
                num_children+=1
            if n.right!=None:
                num_children+=1
            return num_children
        
        #get the pareny of the node to be deleted
        node_parent = node.parent
        #get the number of children to be deleted
        node_children = num_children(node)

        #CASE1 node has no children
        if node_children==0:
            # edge case handled
            if node_parent is None:
                self.ID = None
                self.Name = None
            else:
            #remove refrence to the node from the parent
                if node_parent.left==node:
                    node_parent.left=None
                else:
                    node_parent.right=None
        
        #case2 node has 1 child
        if node_children==1:
            #get the single child node 
            if node.left!=None:
                child=node.left
            else:
                child=node.right 
            
            if node_parent is None:
                # Deleting root node with one child
                # Copy child's data to root and adjust pointers
                self.ID = child.ID
                self.Name = child.Name
                self.left = child.left
                self.right = child.right
                if self.left:
                    self.left.parent = self
                if self.right:
                    self.right.parent = self
            else:
            #replace the node to be deleted with his child
                if node_parent.left==node:
                    node_parent.left=child
                else:
                    node_parent.right=child

                #correct the parent pointer in node 
                child.parent=node_parent

        #case 3 node has two children
        if node_children==2:
            #get the inorder successor of the deleted node 
            successor = min_value_node(node.right)
            #copy the inorder succesor's value to the node formerly holding the value we wish to delete 
            node.ID = successor.ID 
            #delete the successor now that its values was copied into the other node 
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
