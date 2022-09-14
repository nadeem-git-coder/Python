class Dog:
    species = "GS"

    def __init__(self,name ,age):
        self.name = name
        self.age = age

        #instance M
    def delt(self):
        # print(self.name," ",self.age)
        return f" {self.name} is {self.age} years old"
        
    def bark(self,sound):
        # print(self.name," ",sound)
        return f" {self.name} says {sound}"

obj= Dog("Tiger",5)
obj.delt()