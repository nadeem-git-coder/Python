'''
OOP is a method of structuring a program by bundling related properties and beaviours into individual objects

Define a class in Python:-
kirk =["James",34,"Captain",2265]

'''


# class Dog:
#     #class attribute
#     species = "Canis" 

#     def __init__(self,name,age): #Constructor is used to intialize the instances member of the class
#         self.name = name
#         self.age =  age
'''============================================================================================='''
'''
class Student:
    #constructor
    #initiializing instace variable
    def __init__(self,name):
        print('inside construtor')
        self.name = name
        print('instance variable initialized')

    #instance Methods
    def show(self):
        print('My name is ', self.name)
        '''
'''============================================================================================='''
#create object using constructor
# ob1 = Student()
''' 
File "d:\python\oops\Dog.py", line 31, in <module>
    ob1 = Student()
TypeError: __init__() missing 1 required positional argument: 'name'
'''
# ob1 = Student("Nadeem")
# ob1.show()
'''
output :-
inside construtor
instance variable initialized
My name is  Nadeem
'''
'''============================================================================================='''
#Types of constructor
#1 . Default 
'''class Student:
    #constructor
    #initiializing instace variable
    
    #instance Methods
    def show(self):
        print('My name is ')'''
#2. Parameterized
'''
class Student:
    #constructor
    #initiializing instace variable
    def __init__(self,name):
        print('inside construtor')
        self.name = name
        print('instance variable initialized')

    #instance Methods
    def show(self):
        print('My name is ', self.name)'''
#2. Non - parameterizeed
'''
class Student:
    #constructor
    #initiializing instace variable
    def __init__(self):
        print('inside construtor')
        print('instance variable initialized')

    #instance Methods
    def show(self):
        print('My name is ')'''

'''============================================================================================='''


#Constuctor with default values:-----
'''
class Student:
    #constructor
    #initiializing instace variable
    def __init__(self,name,age=16):
        print('inside construtor')
        self.name = name
        self.age = age
        print('instance variable initialized')

    #instance Methods
    def show(self):
        print('My name is ', self.name,self.age)  '''  

# ob = Student("Nadeem",19)
# ob.show()
# ob = Student("Nadeem")
# ob.show()
# ob = Student("John",19)
# ob.show()
'''
inside construtor
instance variable initialized
My name is  Nadeem 19
inside construtor
instance variable initialized
My name is  Nadeem 16
inside construtor
instance variable initialized
My name is  John 19'''
'''============================================================================================='''

'''
class Student:
    #constructor
    #initiializing instace variable
    def __init__(self,name,age):
        print('inside construtor 1')
        self.name = name
        self.age = age
        
    def __init__(self,name):
        print('inside construtor 2')
        self.name = name



    #instance Methods
    def show(self):
        print('My name is ', self.name,self.age)'''

# ob = Student("Nadeem",19)
# ob.show()
'''File "d:\python\oops\Dog.py", line 138, in <module>
    ob = Student("Nadeem",19)
TypeError: __init__() takes 2 positional arguments but 3 were given'''
# ob = Student("Nadeem")
'''inside construtor 2'''

'''============================================================================================='''
#Constructor Chaining
# It is a process of calling one constructor from another constructor
# It is useful when you invoke multiple constructor one after the another by initializing onle one inatance
# for invoking the base class constructor form derived class we use super constructor

'''Inheritance----
class Vehicle:
    def __init__(self,eng):
        print("inside Vehicle const")
        self.eng=eng
class Bike (Vehicle):
    def __init__(self,eng,speed):
        super().__init__(eng)
        print('inside Bike class')
        self.speed = speed
class EBike(Bike):
    def __init__(self,eng,speed,price):
        super().__init__(eng,speed)
        print('inside EBike class')
        self.price = price '''
# eb = EBike('850cc',130,75000)
'''inside Vehicle const
inside Bike class
inside EBike class'''
# print(eb.eng)
'''850cc'''

'''============================================================================================='''















        