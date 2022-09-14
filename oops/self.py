# class Mobile:
#     def display(self):
#         print("Displaying details")

#     def purchase(self):
#         self.display()
#         print("Calculating price")

# Mobile().purchase()

# class Mobile:
#     def __init__(self,price,brand):
#         print("Mobile Created with id", id(self))
#         self.price = price
#         self.brand = brand

#     def return_product(self):
#         print("Mobile being returned has id",id(self))
#         print("Brand being returned is " ,self.brand, 'and price is',self.price)

# mob1= Mobile(1000,"Apple")
# mob2 = Mobile(2000,"redmi")
# Mobile.return_product(mob2)


# class shoe :
#     def __init__ (self,price,material):
#         self.price = price
#         self.material =material
#     def show(self):
#         print(self.price,self.material)

#     def __str__(self):
#         return "Shoe with price: "  + str(self.price) + " and material " + self.material
# ob = shoe(1000,"abc")
# print(ob)

# class Athelete:
#     def __init__(self,name,gender):
#         self.name = name

#         self.gender = gender

#     def set_name(self,name):
#         self

#     def running(self):
#         if (self.gender=="girl"):
#             print("150mtr running")
#         else:
#             print("200mtr running")

# ob = Athelete("Name","M")
# print(ob)


# class Mobile:
#     def _init_(self,brand,price):
#         self.brand = brand
#         self.price = price

# mob1=Mobile("Apple", 1000)
# mob2=Mobile("Samsung", 5000)
# mob3=Mobile("Apple", 3000)

# mob_dict={
#           "m1":mob1,
#           "m2":mob2,
#           "m3":mob3
#           }

# for key,value in mob_dict.items():
#     if value.price > 3000:
#         print (value.brand,value.price)



# class Vehicle:
#     def _init_(self):
#         self.__vehicle_id = None
#         self.__vehicle_cost = None
#         self.__vehicle_type = None
#         self.__premium_amount = None
#     def set_vehicle_id(self,vehicle_id):
#         self.__vehicle_id=vehicle_id
#     def set_vehicle_cost(self,vehicle_cost):
#         self.__vehicle_cost=vehicle_cost
#     def set_vehicle_type(self,vehicle_type):
#         if vehicle_type=="Two Wheeler" or vehicle_type=="Four Wheeler":
#             self.__vehicle_type = vehicle_type
#         else:
#             print("Invalid Vehicle type")
#     def set_premium_amount(self,premium_amount):
#         self.__premium_amount = premium_amount
#     def get_vehicle_id(self):
#         return self.__vehicle_id
#     def get_vehicle_cost(self):
#         return self.__vehicle_cost
#     def get_vehicle_type(self):
#         return self.__vehicle_type
#     def get_premium_amount(self):
#         return self.__premium_amount
#     def calculate_premium(self):
#         if self.__vehicle_type=="Two Wheeler":
#             self._premium_amount = self._vehicle_cost*0.02
#         elif self.__vehicle_type=="Four Wheeler":
#             self._premium_amount = self._vehicle_cost*0.06
#         else:
#             print("Invalid Vehicle type")
#     def display_vehicle_details(self):
#         print("Vehicle id:",self.__vehicle_id)
#         print("Vehicle Type:",self.__vehicle_type)
#         print("Vehicle Cost:",self.__vehicle_cost)
#         print("Premium Amount:",self.__premium_amount)

# v = Vehicle()
# v.set_vehicle_id(123)
# v.set_vehicle_type("Two Wheeler")
# v.set_vehicle_cost(50000)
# v.calculate_premium()
# v.display_vehicle_details()



# from heapq import nlargest
# class student:
#     def get(self):
#         self.name = input("Enter name: ")
#         self.roll = int(input("Enter roll no.: "))
#         self.marks = [0 for _ in range(5)]
#         print("Enter marks:")
#         for i in range(5):
#             m = int(input())
#             self.marks[i]=m if m>=0 and m<=20 else 0
#         self.per = sum(self.marks)
#         self.lar = nlargest(2,self.marks)
#     def show(self):
#         print("Name: ",self.name)
#         print("Roll: ",self.roll)
#         print("Top 2 scores: ",self.lar)

# n = int(input("Enter no of students"))
# l = [student() for _ in range(n)]
# for i in range(n):
#     l[i].get()
# m = l[0]
# for i in range(1,n):
#     if l[i].per>m.per:
#         m = l[i]
# m.show()


# class person:
#     def _init_(self,name,add):
#         self.name=name
#         self.add=add
#         print("object created successfully")
#     def show(self):
#         pass
# class student(person):
#     def _init_(self):
#         print("object of student class created successfully")
#     def show(self):
#         pass

# p1 = person("nadeem","ballia")

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

#     def return_phone(self):
#         print ("Returning a phone")

# class FeaturePhone(Phone):
#     pass

# class SmartPhone(Phone):
#     def __init__(self, price, brand, camera, os, ram):
#         super().__init__(price, brand, camera)
#         self.os = os
#         self.ram = ram
#         print ("Inside smartphone constructor")

#     def buy(self):
#         print ("Buying a smartphone")

# s=SmartPhone(20000, "Samsung", 12, "Android", 2)

# print(s.os)
# print(s.brand)

# class Product:
#     def review(self):
#         print ("Product customer review")

# class Phone(Product):
#     def _init_(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

#     def return_phone(self):
#         print ("Returning a phone")
    
#     def review(self):
#         print("Phone customer review")

# class SmartPhone(Phone):
#     def review(self):
#         Phone.review(self)
#         Product.review(self)

# s=SmartPhone(20000, "Apple", 12)

# s.buy()
# s.review()
# SmartPhone.mro()

# class point1:
#     def _init_(self,x=1,y=0):
#         self.x=x
#         self.y=y
        
#     def _str_(self):
#         return "({0},{1})".format(self.x,self.y)
#     def _add_(self,obj):
#         x=self.x=obj.x
#         y=self.y=obj.y
#         return point(x,y)
        
    
    
# p_1=point1(2,3)
# p_2=point1(3,4)
# print(p_1)
# print(p_2)
# x=4
# y=3
# print(x+y)
# s1="hi"
# s2=" sumit"
# print(s1+s2)

# class Customer:
#     def _init_(self,name,age,phone_no):
#         self.name=name
#         self.age=age
#         self.phone_no=phone_no
    
#     def purchase(self,payment):
#         if payment.type=="Card":
#             print("By card")
#         elif payment.type=="e-wallet":
#             print("By e-wallet")
#         else:
#             print("By Cash")
    
# class payment:
#     def _init_(self,type):
#         self.type=type
    

# payment1=payment("Card")
# c=Customer("Nadeem",21,9934)



class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")


mob1.purchase()
mob2.purchase()
mob3.purchase()
print(mob1.discount)
print(Mobile.discount)
mob1.discount=40
print(mob1.discount)
print(mob2.discount)
print(Mobile.discount)
mob1.purchase()
mob2.purchase()
print(mob2.__dict__)
print(mob1.__dict__)
print(Mobile.__dict__)
