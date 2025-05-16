from BST import BST
from MaxHeap import MaxHeap

class RequestSystem:
    def __init__(self):
        self.bst_root = None
        self.max_heap = MaxHeap()

    def insert_request(self, id, name, priority):
        print(f"\n[Insert] ID: {id}, Name: {name}, Priority: {priority}")
        if self.bst_root is None:
            self.bst_root = BST(id, name)
        else:
            self.bst_root.insertRequest(id, name)

        self.max_heap.insertHeap(id, priority)

    def search_request(self, id):
        print(f"\n[Search] ID: {id}")
        if self.bst_root:
            return self.bst_root.searchRequest(id)
        else:
            print("BST is empty.")
            return None

    def delete_request(self, id):
        print(f"\n[Delete] ID: {id}")
        if self.bst_root:
            self.bst_root.deleteRequest(id)
        else:
            print("BST is empty.")

        # Delete from MaxHeap
        self.delete_from_heap(id)

    def delete_from_heap(self, id):
        found = False
        new_heap = []

        for item in self.max_heap.heap:
            if item[0] != id:
                new_heap.append(item)
            else:
                found = True

        self.max_heap.heap = new_heap

        if found:
            # Re-heapify after deletion
            for i in range(len(self.max_heap.heap) // 2, -1, -1):
                self.max_heap.maxHeapify(i)
            print(f"Request ID {id} removed from MaxHeap.")
        else:
            print(f"Request ID {id} not found in MaxHeap.")
    
    def process_highest_priority(self):
        print("\n[Process] Highest Priority Request")
        max_item = self.max_heap.deleteMaxHeap()
        if max_item:
            id = max_item[0]
            print(f"Processing ID: {id}, Priority: {max_item[1]}")
            if self.bst_root:
                self.bst_root.deleteRequest(id)
        else:
            print("No request to process.")
    

    def increase_priority(self, id, new_priority):
        print(f"\n[Increase Priority] ID: {id}, New Priority: {new_priority}")
        self.max_heap.increasePriority(id, new_priority)

    def print_all(self):
        print("\n--- BST ---")
        if self.bst_root:
            self.bst_root.printBST()
        else:
            print("BST is empty.")

        print("\n--- MaxHeap ---")
        self.max_heap.printMaxHeap()


system = RequestSystem()

system.insert_request(10, "Ali", 3)
system.insert_request(5, "Sara", 5)
system.insert_request(20, "Reza", 1)

system.print_all()

system.search_request(5)

system.increase_priority(20, 6)

system.process_highest_priority()

system.delete_request(10)

system.print_all()

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


