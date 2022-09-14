
class BinaryTreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#levelwise Input Binary Tree
import queue
def levelwiseTreeInput():
    q = queue.Queue()
    print("Enter Root")
    rootData = int(input())
    if rootData ==-1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node = q.get()
        print("Enter left child of ",current_node.data)
        leftChildData = int(input())
        if leftChildData !=-1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("Enter right child of ",current_node.data)
        rightChildData = int(input())
        if rightChildData !=-1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)

    return root

def printTreeDetail(root):
    if root ==None:
        return
    print(root.data, " : ",end=" ")
    if root.left != None:
        print("L",root.left.data,end=" ")
    if root.right !=None:
        print("R",root.right.data,end=" ")
    print()
    printTreeDetail(root.left)
    printTreeDetail(root.right)

root = levelwiseTreeInput()


printTreeDetail(root)