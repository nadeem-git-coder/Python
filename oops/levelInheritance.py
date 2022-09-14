# Single Level
''''
class Computer:
    def __init__(self,price,brand):
        print("Inside computer class constructor")
        self.price = price
        self.brand = brand
    def buy(self):
        print("Buying Computer")

    def excahnge(self):
        print("exchanging Computer")
class Laptop(Computer):
    pass
l1 = Laptop(10000,"HP")
l1.buy()
l1.excahnge()'''

# Multilevel Inheritance
'''
class EDevice:
    def type(self):
        print("Electronic Device")

class Computer(EDevice):
    def __init__(self,price,brand):
        print("Inside computer class constructor")
        self.price = price
        self.brand = brand
    def buy(self):
        print("Buying Computer")

    def excahnge(self):
        print("exchanging Computer")
class Laptop(Computer):
    pass
l1 = Laptop(10000,"HP")
l1.buy()
l1.excahnge()
l1.type()
'''
# Hierrarical Inheritance
'''
class EDevice:
    def type(self):
        print("Electronic Device")

class Computer(EDevice):
    def __init__(self,price,brand):
        print("Inside computer class constructor")
        self.__price = price
        self.__brand = brand
    def getter(self):
        print(self.__price,self.__brand)
        
    def buy(self):
        print("Buying Computer")

    def excahnge(self):
        print("exchanging Computer")
class Laptop(Computer):
    pass
class Destop(Computer):
    pass

l1 = Computer(10000,"HP")
l1.buy()
l1.excahnge()
l1.getter()
print(l1.price,l1.brand)


l1 = Laptop(10000,"HP")
l1.buy()
l1.excahnge()
l1.getter()
print(l1.price,l1.brand)


'''
# Multiple Inheritance


# class Computer():
#     def __init__(self,price,brand):
#         print("Inside computer class constructor")
#         self.price = price
#         self.brand = brand
#     # def getter(self):
#     #     print(self.__price,self.__brand)
        
#     def buy(self):
#         print("Buying Computer")

#     def excahnge(self):
#         print("exchanging Computer")
# class EDevice():
#     def type(self):
#         print("Electronic Device")
    

# class Laptop(Computer,EDevice):
#     pass
# class Destop(Computer):
#     pass

# l1 = Laptop(10000,"HP")
# l1.buy()
# l1.excahnge()
# l1.type()
# # l1.getter()
# print(l1.price,l1.brand)

class Computer():
    def __init__(self,price,brand):
        print("Inside computer class constructor")
        self.price = price
        self.brand = brand
    # def getter(self):
    #     print(self.__price,self.__brand)
        
    def buy(self):
        print("Buying Computer")

    def excahnge(self):
        print("exchanging Computer")
class EDevice():
    def type(self):
        print("Electronic Device")
    def buy(self):
        print("Buying Electronic device")
    

class Laptop(EDevice,Computer):
    pass
class Destop(Computer):
    pass

l1 = Laptop(10000,"HP")
l1.buy()
l1.excahnge()
l1.type()
# l1.getter()
print(l1.price,l1.brand)