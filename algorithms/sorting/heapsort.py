class HeapsortClass:
    name = "Heapsort"

    @staticmethod
    def Heapsort(itemsetCom):
        itemset = list(itemsetCom)
        index = len(itemset)-1
        heap = HeapListBased()
        for el in itemset:
            heap.addElement(el)
        output = [0] * len(itemset)
        while index >= 0:
            heap.createMaxHeap()
            heap.replaceNodes(0, index)
            output[index] = heap.deleteNodeAndReturnVal(index)
            index-=1
        return output
# END Heapsort class

class HeapListBased:
    heap = []
    size = 0
    def addElement(self, value):
        if len(self.heap) > 0:
            if value > self.heap[0]:
                tmp = self.heap[0]
                self.heap[0] = value
                value = tmp
        self.heap.append(value)
        self.size += 1
        self.createMaxHeap()
    
    def createMaxHeap(self):
        while not self.isMaxHeap():
            for i in range(int(len(self.heap)/2)):
                left = self.leftNodeID(i)
                if left <self.size:
                    if self.heap[left] > self.heap[i]:
                        self.replaceNodes(left,i)
                right = self.rightNodeID(i)        
                if right <self.size:
                    if self.heap[right] > self.heap[i]:
                        self.replaceNodes(right,i)
    # END create max heap
    def isMaxHeap(self):
        for index in range(self.size):
            left = self.leftNodeID(index)
            if left < self.size and self.heap[left] > self.heap[index]:
                return False
            right = self.rightNodeID(index)
            if right < self.size and self.heap[right] > self.heap[index]:
                return False
        return True
    def leftNodeID(self, parent):
        return 2*parent + 1
    def rightNodeID(self, parent):
        return 2*parent + 2

    def replaceNodes(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp
    def deleteNodeAndReturnVal(self, index):
        val = self.heap[index]
        del self.heap[index]
        self.size -= 1
        return val
#END next Heap try


class Node:
    def __init__(self, val, id):
        self.val = val
        self.id = id
    leftN = None
    rightN = None
class Heap:
    size = 0
    root = None
    def Add(self, value):
        self.size += 1
        if self.root is None:
            self.root = Node(value, self.size - 1)
            return
        queue = [self.root]
        for node in queue:
            if node.leftN is None:
                node.leftN = Node(value, self.size - 1)
                return
            queue.append(node.leftN)
            if node.rightN is None:
                node.rightN = Node(value, self.size - 1)
                return
            queue.append(node.rightN)
        self.optimizeHeap()
    # END add method
    def optimizeHeap(self):
        while not self.isMaxHeap():
            queue = [self.root]
            for node in queue:
                if node.leftN is None:
                    continue
                if node.leftN.val > node.val:
                    self.replaceNodes(node, node.leftN)
                    queue.append(node.leftN)
                if node.rightN is None:
                    continue
                if node.rightN.val > node.val:
                    self.replaceNodes(node, node.rightN)
                    queue.append(node.rightN)
    # END optimize heap method

    def replaceNodes(self, nodeUp, nodeDow):
        tmp = nodeUp.val
        nodeUp.val = nodeDow.val
        nodeDow.val = tmp
    
    def isMaxHeap(self):
        queue = [self.root]
        for node in queue:
            if node.leftN is not None:
                if node.leftN.val > node.val:
                    return False
                queue.append(node.leftN)
            if node.rightN is not None:
                if node.rightN.val> node.val:
                    return False
                queue.append(node.rightN)
        return True
        
    def removeLastNode(self):
        lastRef= self.fidViaID(self.size-1)
        self.size -=1
        valToRet = self.root.val
        self.replaceNodes(self.root, lastRef)
        lastID = lastRef.id
        if (lastID %4) % 2 == 0:
            parentID = int((lastID-2)/2)
            if parentID >= 0: 
                paretnRef = self.fidViaID(parentID)
                paretnRef.rightN = None
        elif (lastID %4) % 2 == 1:
            parentID = int((lastID-1)/2)
            if parentID >= 0: 
                paretnRef = self.fidViaID(parentID)
                paretnRef.leftN = None
        return valToRet


    def fidViaID(self, ID):
        lastRef= None
        queue = [self.root]
        for node in queue:
            if node.leftN is not None:
                queue.append(node.leftN)
            if node.rightN is not None:
                queue.append(node.rightN)
            if node.id == ID:
                lastRef = node
        return lastRef

        
            
