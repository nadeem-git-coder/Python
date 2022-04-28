from urllib.request import ProxyBasicAuthHandler


class Node:
    def __init__(self,d):
        self.data =d
        self.next = None
class MyStack:
    def __init__(self):
        self.head= None
        self.sz =0
    def push(self,x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.sz =self.sz +1

    def size(self):
        return self.sz
    def pop(self):
        if(self.head==None):
            return None
        res = self.head.data
        self.sz= self.sz-1
        self.head = self.head.next
        return res
    def peek(self):
        if(self.head==None):
            return None
        p= self.head.data
        return p
    def display(self):
        curr = self.head
        while curr!= None:
            print(curr.data,"->",end=' ')
            curr = curr.next
        print("None")

#Driver code

ch=0
s=MyStack()

while ch!=6:
    print("---------------------------")
    print("Press 1 for Push operation")
    print("Press 2 for Pop operation ")
    print("Press 3 for Peek opreation")
    print("Press 4 for Size of Stack")
    print("Press 5 for Dispaly")
    print("---------------------------")
    print("Enter Your Choice:- ")
    ch = int(input())
    
    if ch==1:
        x= int(input("Enter the data : "))
        s.push(x)
    elif ch==2:
        r =s.pop()
        print("Popped data : ",r)
    elif ch==3:
        r =s.peek()
        print("Peek  : ",r)
    elif ch==4:
        r =s.size()
        print("Size : ",r)
    elif ch==5:
        s.display()
    else:
        break





        