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
                print(f"\n{id} do not exists.\n")
                return None
            else:
                return self.right.searchRequest(id)
        else:
            print(f"\nfound.\n ID: {id}, name: {self.Name}\n")
            return self
                
    
    def delete_value(self, id):
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









# tree = BST(10,'a')
# tree.insertRequest(5,'b')
# tree.insertRequest(4,'c')
# tree.insertRequest(2,'d')
# tree.insertRequest(1,'e')
# tree.insertRequest(3,'f')
# tree.insertRequest(22,'g')
# tree.insertRequest(11,'h')
# tree.insertRequest(12,'i')
# tree.printBST()
# tree.delete_value(22)
# tree.delete_value(13)
# tree.delete_value(11)
# tree.printBST()

# tree.searchRequest(22)
# tree.searchRequest(1)
# tree.searchRequest(6)


