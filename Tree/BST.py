
class BinaryTreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None




# Recursive BST Insertion
def insertBST(root,key):
    if root ==None:
        return BinaryTreeNode(key)
    if root.data == key:
        return root
    elif root.data > key:
        root.left = insertBST(root.left,key)
    else:
        root.right = insertBST(root.right,key)
    return root

# Iterative BST Insertion
def insertIterativeBST(root,key):
    curr = root
    parent = None
    while curr !=None:
        parent = curr
        if curr.data ==key:
            return root
        
        elif curr.data >key:
            curr = curr.left
        else:
            curr = curr.right

    if parent==None:
        return BinaryTreeNode(key)
    if parent.data > key:
        parent.left = BinaryTreeNode(key)
    else:
        parent.right = BinaryTreeNode(key)
    return root
def getSucc(curr,key):
    
    while curr.left!=None:
        curr=curr.left
    return curr.data
# Recursive BST Deletion
def deleteBST(root,key):
    if root==None:
        return 
    if root.data > key:
        root.left = deleteBST(root.left,key)
    elif root.data <key:
        root.right = deleteBST(root.right,key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = getSucc(root.right,key)
            root.data = succ
            root.right = deleteBST(root.right,succ)
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

root = None
for i in range(5):
    n = int(input("Enter the data : "))
    # root = insertBST(root,n)
    root=insertIterativeBST(root,n)


printTreeDetail(root)
deleteBST(root,10)
printTreeDetail(root)