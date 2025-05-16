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
    
    def isEmptyBST(self):
        return self is None  

    def sizeBST(self):
        count = 1
        if self.left:
            count += self.left.sizeBST()
        if self.right:
            count += self.right.sizeBST()
        return count



class MaxHeap:
    def __init__(self):
        self.heap = []  

    def insertHeap(self, id, priority):
        self.heap.append((id, priority))
        self.heapify_up(len(self.heap) - 1)

    def deleteMaxHeap(self):
        if len(self.heap) == 0:
            print("Heap is empty.")
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_request = self.heap[0]
        self.heap[0] = self.heap[-1] # assign root with last item
        self.heap.pop()
        self.maxHeapify(0)
        return max_request

    # def processHighestPriorityRequest(self, bst_root):
    #     max_item = self.deleteMaxHeap()
    #     if max_item:
    #         id = max_item[0]
    #         print(f"\nProcessing request ID: {id}, Priority: {max_item[1]}")
    #         bst_root.deleteRequest(id)
    #     else:
    #         print("No request to process.")

    def printMaxHeap(self):
        print("\n")
        for id, priority in self.heap:
            print(f"ID: {id}, Priority: {priority}")

    def maxHeapify(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self.heap)

        if left < size and self.heap[left][1] > self.heap[largest][1]:
            largest = left
        if right < size and self.heap[right][1] > self.heap[largest][1]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]# swap
            self.maxHeapify(largest)

    def increasePriority(self, id, newPriority):
        for i in range(len(self.heap)):
            if self.heap[i][0] == id:
                if newPriority > self.heap[i][1]:
                    self.heap[i] = (id, newPriority)
                    self.heapify_up(i)
                    print(f"Priority updated for ID: {id}")
                else:
                    print("New priority must be higher than current.")
                return
        print(f"Request with ID {id} not found.")

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][1] > self.heap[parent_index][1]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break


    def isEmptyHeap(self):
        return len(self.heap) == 0

    def sizeMaxHeap(self):
        return len(self.heap)


# heap = MaxHeap()
# heap.insertHeap(101, 5)
# heap.insertHeap(102, 9)
# heap.insertHeap(103, 3)

# heap.printMaxHeap()

# heap.increasePriority(103, 10)
# heap.printMaxHeap()

# heap.deleteMaxHeap()
# heap.printMaxHeap()







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
# tree.deleteRequest(22)
# tree.deleteRequest(13)
# tree.deleteRequest(11)
# tree.printBST()

# tree.searchRequest(22)
# tree.searchRequest(1)
# tree.searchRequest(6)


