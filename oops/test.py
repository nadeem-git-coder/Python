'''class Dog:
    species = "GS"

    def __init__(self,name ,age):
        self.name = name
        self.age = age

        #instance M
    def details(self):
        # print(self.name," ",self.age)
        return f" {self.name} is {self.age} years old"
        
    def bark(self,sound):
        # print(self.name," ",sound)
        return f" {self.name} says {sound}"

obj= Dog ("Tiger",5)
obj.details()
obj.bark("woof woof")
Tiger   5
Tiger   woof woof
'''
# class Dog:
#     species = "GS"

#     def __init__(self,name ,age):
#         self.name = name
#         self.age = age

#         #instance M
#     def __str__(self):
#         # print(self.name," ",self.age)
#         return f" {self.name} is {self.age} years old"
        
#     def bark(self,sound):
#         # print(self.name," ",sound)
#         return f" {self.name} says {sound}"

# obj= Dog("Tiger",5)

#types
# 1. private - only accessiable to class itself
# 2. public -  accessiable to all (inside and ouside pakages)
# 3. protected - which are accessiable only by inherited classes
# 4. default - accesssiable by all the modules inside the packages but not accessiable by the outside package


