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
