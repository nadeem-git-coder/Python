# #Divtionary of objects
# class Computer:
#     def __init__(self,price1,ver1):
#         self.price = price1
#         self.ver = ver1
    
# c1 = Computer(90000,4.2)
# c2 = Computer(100000,1.3)
# c3 = Computer(60000,2.6)
# c4 = Computer(70000,3.9)
# c5 = Computer(80000,4.2)
# l1 = [c1,c2,c3,c4,c5]
# d1={}
# for item in l1:
#     d1[item.ver] = item.price
# print(l1)
# print('----------------------')

# for key, val in d1.items():
#     print(key,val)


# class Computer:
#     def __init__(self,brand,price,ram,storage):
#         self.brand  = brand
#         self.price = price
#         self.ram = ram
#         self.storage = storage

#     def buy(self):
#         print("buying computer")
#     def run(self):
#         pass
#     def sell(self):
#         pass
#     def compute(self):
#         pass

# class Laptop(Computer):
#     def __init__(self,battery,carry):
#         self.battery = battery
#         self.carry = carry
#     def exchange(self):
#         print("wnat to exchange ut computer")

# l1 = Laptop("HP",90000,16,512)
# l1.exchange()    
# l1.buy() 


class Computer:
    def __init__(self,brand,price,ram,storage):
        self.brand  = brand
        self.price = price
        self.ram = ram
        self.storage = storage

    def buy(self):
        print("buying computer")
    def run(self):
        pass
    def sell(self):
        pass
    def compute(self):
        pass

class Laptop(Computer):

    def __init__(self,battery,carry,c1):
        super().__init__(c1.brand,c1,price,c1.ram,c1.storage)

        self.battery = battery
        self.carry = carry
    def exchange(self):
        print("wnat to exchange ut computer")
    def buy(self):
        super().buy()
        prrnt("Buying ")

l1 = Laptop("HP",90000,16,512)
l1.exchange()    
l1.buy() 


