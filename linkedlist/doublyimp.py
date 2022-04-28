

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        self.prev = None

def InsertBeg(head):
    k = int(input("Enter the data : "))
    temp = Node(k)
    if head!=None:
        head.prev = temp
    temp.next = head
    return temp

def InsertEnd(head):
    k = int(input("Enter the data : "))
    temp = Node(k)
    if head== None:
        return temp
    curr = head
    while curr.next!=None:
        curr = curr.next
    curr.next = temp
    temp.prev = curr
    return head

def DeleteFirst(head):
    if(head==None):
        return None
    elif(head.next==None):
        return None
    else:
        head = head.next
        return head   
def DeleteEnd(head):
    if(head==None):
        return None
    elif(head.next ==None):
        return None
    else:
        curr = head 
        while curr.next.next != None:
            curr = curr.next
        curr.next=None
        return head

def DeleteAtpos(head,x):
    if(head == None):
            return None
    elif(x==1):
        head = head.next
        head.prev = None
        return head
            
            
    else:
        curr = head
        for i in range(x-2):
            curr = curr.next
        curr.next = curr.next.next
            
           
        return head

def rev(head):
    if (head== None):
        return None
    elif(head.next== None):
        return head
    else:
        prev = None
        curr =head
        while curr != None:
            prev = curr 
            curr.next , curr.prev = curr.prev , curr.next
            curr = curr.prev
        return prev
        


def Display(head):
    curr = head
    print("None <-",end=" ")
    while curr!=None:
        print(curr.key,"<-->",end=" ")
        curr = curr.next
    print("None")

#Driver Code
head = None
ch=0
while(ch!=7):
    print("Press 1 for Display")
    print("Press 2 for InsertBeg")
    print("Press 3 for InsertEnd")
    print("Press 4 for DeleteFirst")
    print("Press 5 for DeleteEnd")
    print("Press 6 for DeleteAtPos")
    print("Press 7 for ReverseLL")

    print("Enter your Choice ")
    ch = int(input())
    if(ch==1):
        Display(head)
    elif(ch==2):
        head = InsertBeg(head)
    elif(ch==3):
        head = InsertEnd(head)
    elif(ch==4):
        head=DeleteFirst(head)
    elif(ch==5):
        head = DeleteEnd(head)
    elif(ch==6):
        pos = int(input("Enter the pos"))
        head = DeleteAtpos(head,pos)

    elif(ch==7):
        head = rev(head)
    else:
        break

