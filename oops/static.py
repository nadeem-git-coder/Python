# class Computer:
#     def __init__(self,price1,ver1,brand1):
#         self.price = price1
#         self.ver = ver1
#         self.brand = brand1


# def display(l1):
#     for i in l1:
#         print(i.price,i.ver,i.brand)
    

# c1 = Computer(90000,3.5,"HP")
# c2=  Computer(80000,4.5,"HP")
# c3 = Computer(70000,6.5,"HP")
# c4 = Computer(60000,3.2,"HP")
# c5 = Computer(140000,1.5,"HP")

# l1 = [c1,c2,c3,c4,c5]
# display(l1)
'''
class Computer:
    brand = "HP"
    def __init__(self,price1,ver1):
        self.price = price1
        self.ver = ver1
        # self.brand = brand1


def display(l1):
    for i in l1:
        print(i.price,i.ver,Computer.brand)
        # print(i.price,i.ver,i.brand)
    

c1 = Computer(90000,3.5)
c2=  Computer(80000,4.5)
c3 = Computer(70000,6.5)
c4 = Computer(60000,3.2)
c5 = Computer(140000,1.5)

l1 = [c1,c2,c3,c4,c5]
display(l1)'''

# static
'''
class Computer:
    brand = "HP" #static Variable
    cno= 0
    def __init__(self,price1,ver1):
        Computer.cno = Computer.cno +1 
        self.sno = Computer.cno
        self.price = price1
        self.ver = ver1
        # self.brand = brand1


def display(l1):
    for i in l1:
        print(i.price,i.ver,Computer.brand)
        # print(i.price,i.ver,i.brand)
    
def updateBrand(a):
    Computer.brand = a
c1 = Computer(90000,3.5)
c2=  Computer(80000,4.5)
c3 = Computer(70000,6.5)
c4 = Computer(60000,3.2)
c5 = Computer(140000,1.5)

l1 = [c1,c2,c3,c4,c5]
display(l1)
updateBrand("HP++")
display(l1)'''

class Computer:
    __brand = "HP" #static Variable
    cno= 0
    def __init__(self,price1,ver1):
        Computer.cno = Computer.cno +1 
        self.sno = Computer.cno
        self.price = price1
        self.ver = ver1
        # self.brand = brand1
    @staticmethod
    def getBrand():
        return Computer.__brand

    @staticmethod
    def setBrand(brand1):
        Computer.__brand = brand1


def display(l1):
    for i in l1:
        print(i.price,i.ver,Computer.getBrand())
        # print(i.price,i.ver,i.brand)


    
def updateBrand(a):
    Computer.brand = a
c1 = Computer(90000,3.5)
c2=  Computer(80000,4.5)
c3 = Computer(70000,6.5)
c4 = Computer(60000,3.2)
c5 = Computer(140000,1.5)

l1 = [c1,c2,c3,c4,c5]
display(l1)
updateBrand("HP++")
Computer.setBrand("HP++")
display(l1)