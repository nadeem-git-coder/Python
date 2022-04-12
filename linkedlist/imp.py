from curses import KEY_SELECT


class Node:
    def __init__(self,key):
        self.key  = key 
        self.next = None

def dis(head):
    cur = head
    while(cur!=None):
        print(cur.key)
        cur = cur.next

def insertatbeg(head,key):
    temp = Node(key)

    temp.next = head
    temp = head
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
insertatbeg(head,5)
dis(head)


