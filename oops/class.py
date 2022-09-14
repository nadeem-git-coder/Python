class calc:
    def add(self,a,b):
        self.a =a
        self.b =b
        print("add ",self.a + self.b)

    def sub(self,a,b):
        self.a = a
        self.b = b
        print("sub ",self.a - self.b)
    
    def multiply (self,a,b):
        self.a = a
        self.b = b
        print("mul ",self.a * self.b)
    def divide (self,a,b):
        self.a = a
        self.b = b
        print("div ",self.a/self.b)


while True:
    print("--------------------------")
    print("Press 1 for add")
    print("Press 2 for sub")
    print("Press 3 for multiply")
    print("Press 4 for divide")
    print("Enter Your Choice")
    print("--------------------------")
    ch = int(input())
    

    if ch==1:
        a = int(input("Enter num a :"))
        b = int(input("Enter num b :"))

        calc1 = calc()
        calc1.add(a,b)
    elif ch==2:
        a = int(input("Enter num a :"))
        b = int(input("Enter num b :"))

        calc2 = calc()
        calc2.sub(a,b)
    elif ch==3:
        a = int(input("Enter num a :"))
        b = int(input("Enter num b :"))


        calc3 = calc()
        calc3.multiply(a,b)
    elif ch==4:
        a = int(input("Enter num a :"))
        b = int(input("Enter num b :"))
        calc4 = calc()
        calc4.divide(a,b)
    else:
        break