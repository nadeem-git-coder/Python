'''class Node:
    def __init__(self,key):
        self.key  = key 
        self.next = None

def dis(head):
    cur = head
    while(cur!=None):
        print(cur.key,"->",end=" ")
        cur = cur.next
    print("None")
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

head = None
head= insertEnd(head)
dis(head)'''




class Node:
    def __init__(self,key):
        self.key  = key 
        self.next = None




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
        


head = None
ch =0
while ch!=2:
    print("Press 1 for InsertBeg")
    print("Press 2 for InsertEnd")
    print("Press 3 for  Display")
    print("Enter your choice : ")

    ch = int(input())
    if(ch==1):
        
        head =insertatbeg(head)
    elif(ch==2):

        head =insertEnd(head)
    elif(ch==3):
        dis(head)
    else:
        break
    

