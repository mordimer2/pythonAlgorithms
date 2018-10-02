class TreeSortClass:
    name = "Tree sort"
    @staticmethod
    def TreeSort(itemsetCom):
        itemset = list(itemsetCom)
        binTree = BinaryTree()
        for item in itemset:
            binTree.Add(item)
        itemset = binTree.getinorderList()
        binTree.DestroyTree()
        return itemset
# END TreeSortClass

class Node:
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
# END Node class

class BinaryTree:
    def __init__(self):
        self.root = None
        self.__inorder = []

    def Add(self, element):
        if self.root == None:
            self.root = Node(element)
            return
        self.add(self.root, element)
    
    def add(self,nodeRef , element):
        if nodeRef.value > element:
            if nodeRef.leftNode == None:
                nodeRef.leftNode = Node(element)
                nodeRef.leftNode.value = element
                return
            self.add(nodeRef.leftNode, element)
        else:
            if nodeRef.rightNode == None:
                nodeRef.rightNode = Node(element)
                nodeRef.rightNode.value = element
                return
            self.add(nodeRef.rightNode, element)
    # END add element to binary tree
    
    def getinorderList(self):
        self.initializeinorderList(self.root)
        return self.__inorder
    def initializeinorderList(self, nodeRef):
        if nodeRef == None:
            return
        if nodeRef.leftNode == None and nodeRef.rightNode == None:
            self.__inorder.append(nodeRef.value)
            return
        if nodeRef.leftNode != None:
            self.initializeinorderList(nodeRef.leftNode)
        self.__inorder.append(nodeRef.value)
        if nodeRef.rightNode != None:
            self.initializeinorderList(nodeRef.rightNode)

    def DestroyTree(self):
        self.destroyTree(self.root)
    def destroyTree(self, nodeRef):
        if nodeRef == None:
            return
        if nodeRef.leftNode == None and  nodeRef.rightNode == None:
            nodeRef = None
            return
        if nodeRef.leftNode != None:
            self.destroyTree(nodeRef.leftNode)
        if nodeRef.rightNode != None:
            self.destroyTree(nodeRef.rightNode)
    # END Destroy Tree
# END Binary Tree