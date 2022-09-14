#Delecartion of class of Binary Tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =None
        
#Printing of Binary Tree
def printTree(root):
    if root==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

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

#Number of Nodes 
def numNodes(root):
    if root ==None:
        return 0
    leftNode = numNodes(root.left)
    rightNode  = numNodes(root.right)
    return 1 + leftNode + rightNode

#Sum of nodes 
def sumNodes(root):
    if root ==None:
        return 0
    leftNode = sumNodes(root.left)
    rightNode = sumNodes(root.right)
    return leftNode + rightNode + root.data


#Input of Binary Tree
def treeInput():
    rootData = int(input("Enter the data : "))
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    print("Enter left data : ")
    leftTree = treeInput()
    print("Enter right data : ")
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root    


#Driver Code :-

root = treeInput()

printTree(root)
printTreeDetail(root)
numNodes(root)
sumNodes(root)