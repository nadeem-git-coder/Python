
class Node:
    def __init__(self,key):
        self.key  = key 
        self.next = None

def deleteFirst(head):
    if(head==None):
        return None
  
    return head.next

def deleteLast(head):
    if(head==None):
        return None
    if (head.next==None):
        return None

    curr  = head
    while curr.next.next !=None:
        curr = curr.next
    curr.next = None
    return head

def deleteAtPos(head):
    pos = int(input("Enter the postion to be delete"))
    if(head==None):
        
        return None
    if(pos==1 ):
        return deleteFirst(head)
    curr = head
    for i in range(pos-2):
        curr = curr.next
        
    curr.next = curr.next.next
    return head
    

def inserAtPos(head):
    pos = int(input("Enter position"))
    k = int(input("Enter element"))
    temp = Node(k)
    if pos==1:
        temp.next = head
        return temp
    curr = head
    for i in range(pos-2):
        curr = curr.next
        if(curr==None):
            return head
    temp.next = curr.next
    curr.next =temp
    return head
    

def dis(head):
    cur = head
    while(cur!=None):
        print(cur.key,"->",end=" ")
        cur = cur.next
    print("None")

def insertatbeg(head):
    k = int(input("Enter element : "))
    temp = Node(k)

    temp.next = head
    
    return temp
def insertEnd(head):
    k = int(input("Enter element"))

    temp = Node(k)
    if(head==None):

        return temp
   
    curr = head
    while curr.next!= None:
            curr = curr.next
    
    curr.next = temp 

    return head

def rev(head):
    stack =[]
    curr = head
    while curr!=None:
        stack.append(curr.key)
        curr = curr.next
    curr = head 
    while curr!= None:
        curr.key = stack.pop()
        curr= curr.next

    return head

        


head = None
ch =0
while ch!=9:
    print("Press 1 for InsertBeg")
    print("Press 2 for InsertEnd")
    print("Press 3 for  Display")
    print("Press 4 for InsertAtPos")
    print("Press 5 for DeleteFirst")
    print("Press 6 for DeleteLast")
    print("Press 7 for DeleteAtPos")
    print("Press 8 for Reverse LL")
    print("Enter your choice : ")

    ch = int(input())
    if(ch==1):
        
        head =insertatbeg(head)
    elif(ch==2):
        head=insertEnd(head)
    elif(ch==3):
        dis(head)
    elif(ch==4):
        head = inserAtPos(head)
    elif(ch==5):
        head = deleteFirst(head)
    elif(ch==6):
        head = deleteLast(head)
    elif(ch==7):
        head = deleteAtPos(head)
    elif(ch==8):
        head = rev(head)
    else:
        break
    

