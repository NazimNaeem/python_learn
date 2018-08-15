# task5: revise concept for
# - declaring definitions (methods)
# - calling methods.
# - giving different kind of parameters to methods.
# - giving parameters by reference (which is default in python.)
# - how to pack parameters e.g. myfunc(param1, param2, *param3) how to call methods like that and what kind of params can we give in place of param3 and how to use it inside that method?
# - similarly myfunc(param1, param2, *param3) how to call methods like that and what can we pass for param2 and param3? how to use param2 and param3 inside that method?
# - how to figure out method variables and global variables? how to use /update global variables inside methods?
# - how to return different kind of objects in a method? how to return a dict / list / tuple method and how to use them?

# - how to declare classes?
# - how to declare child classes?
# - how to inherit class from more than one parent class?
# - how to override a parent method?
# - how to extend a parent method? (call parent method first and then extend by overriding.)
# - how to set instance members / static members / class members?
# - how to initialize a class?
# - how to update class member / static member / instance member after initializing?
# - how to overload operators. e.g. you make a class `Line` that has a member `length`. you have two Line classes in variable `a` and `b` and when you add them like `a + b` you should be returned length of class in variable `a` + the length of class in variable `b` (that's called overloading: you define a custom functionality for a basic operator `+` in this case)
# - how to print your custom class? e.g. if you print a class like `a = Line(); print(a)` it should print a message of your choice.
# - if class `C` is inherited from `A`, `B` both and `A`, `B` classes have a method `hello` then when you call `hello` method of `C` class, which one will be called and why?
#   `class C(A, B) <- class definition
#    c = C(); c.hello() <- will this be a `hello` of A class or B class?`
# - how to declare private methods in a class?
# - a python class can have variables like `_var1` and `__var2` (single underscor and double underscore) what kind of methods are they and how to use / update them?

# - how to import a class from other script?
# - how to import a method from other script?
# - how to use relative import and absolute import?
# - how to make a package in python?



# ===================================================================================================================
# - declaring definitions (methods)
# ===================================================================================================================

# def sum(num1, num2):
	
# 	print("Sum is equal to %d" % (int(num1) +int(num2)))

# number1 = input("Enter the first number :")
# number2 = input("Enter the second  number :")
# sum(number1, number2)						calling methods.

# ===================================================================================================================
# - giving different kind of parameters to methods.
# ===================================================================================================================

# def per_info(name, age):					
# 	print("%s you are %d year old" %(name,age))

# name = input("Enter your name :")
# age = int(input("Enter your age  :"))
# per_info(name, age)

# ===================================================================================================================
# - giving parameters by reference (which is default in python.)
# ===================================================================================================================

# def square(number):	
# 	number +=[item*item for item in number]	
# number = [0,1,2,3,4,5,6]
# print (number)
# square(number)
# print(number)


# ===================================================================================================================
# - how to pack parameters e.g. myfunc(param1, param2, *param3) how to call methods like that and what kind of params
# - can we give in place of param3 and how to use it inside that method?
# ===================================================================================================================


# def myfunc(name, roll_no, *marks):
# 	count = 0
# 	print("Name: %s \nRoll_no: %s"% (name,roll_no))
# 	for mark in marks:
# 		count += 1
# 		print("Subject %d marks = %s"% (count,mark))

# myfunc("Nazim",1303,70,75,75.0,65.1)

# ===================================================================================================================
# - how to figure out method variables and global variables?
# ===================================================================================================================

# def myfunc(roll_no, *marks):
# 	count = 0                 # count is method variable
# 	print("Name: %s \nRoll_no: %s"% (name,roll_no))
# 	for mark in marks:
# 		count += 1
# 		print("Subject %d marks = %s"% (count,mark))

# global name                   # By declare global keyword with variable 
# name = "Nazim"
# myfunc(1303,70,75,75.0,65.1)


# ===================================================================================================================
# - how to return different kind of objects in a method?
# ===================================================================================================================

# - How to return list

# def square(number):	
# 	number = [item*item for item in number]	
# 	return number
# number = [0,1,2,3,4,5,6]
# print(square(number))

# - How to return Dictionary

# def myfunc():	
# 	dic = {'Name': 'Nazim', 'Age': 7, 'Class': 'First'}
# 	return dic
# dictionary=myfunc()
# for key, value in dictionary.items():
#     print(key, value)


# - How to return Dictionary

# def myfunc():	
# 	tup = ('Nazim',7)
# 	return tup
# tup1=myfunc()
# for value in tup1:
#     print(value)

# ===================================================================================================================
# - how to declare classes?
# ===================================================================================================================

# class Animal:
#    aniCount = 0  # static member

#    def __init__(self, name):
#       self.name = name
#       Animal.aniCount += 1
   
#    def displayCount(self):
#      print("Total Animal %d" % (Animal.aniCount))
#    def displayAnimal(self):
#       print("Name : %s " %(self.name))

# Use for  Animal class only

# ani1 = Animal("cat")
# ani1.displayAnimal()
# ani2 = Animal("dog")
# ani2.displayAnimal()
# print("Total Animal : %d"%(Animal.aniCount))


# ===================================================================================================================
# - how to declare child classes?
# ===================================================================================================================

# class cat(Animal):
#   pass

# # Use for child class cat  only 
# # obj = cat("persion")
# # obj.displayAnimal()

# ===================================================================================================================
# - how to inherit a class form more than one parent?
# ===================================================================================================================

# class Elephant:
#   def __init__(self, legs):
#      self.legs = legs
  
#   def displaylegs(self):
#     print("This animal have %d  legs" %(self.legs))

#   def display(self):
#     print("This Animal is Elephant")

# class Dog(Animal,Elephant):
#   def display(self):
#     # super().display()     # Use to extend parent method
#     print("This Animal is Dog")

# obj = Dog("German")
# obj.legs = 4
# obj.displayAnimal()
# obj.displaylegs()

# ===================================================================================================================
# - how to override a parent method?
# ===================================================================================================================

# obj = Dog("German")
# obj.display()

# ===================================================================================================================
# - how to extend a parent method? (call parent method first and then extend by overriding.)
# ===================================================================================================================

# Line 183 extend  a parent method

# ===================================================================================================================
# - how to overload operators. e.g. you make a class `Line` that has a member `length`.
# - you have two Line classes in variable `a` and `b` and when you add them like `a + b` 
# - you should be returned length of class in variable `a` + the length of class in variable `b` 
# - (that's called overloading: you define a custom functionality for a basic operator `+` in this case)
# ===================================================================================================================

class Line:
 
    def __init__(self, length):
        self.length = length

# # - how to print your custom class? e.g. if you print a class like `a = Line(); print(a)` 
# # - it should print a message of your choice.
    def __repr__(self):
        return 'The name of the class is Line'
 
    def setlength(self, length):
        self.length = length
 
    def getlength(self):
        return self.length
 
    def __add__(self, another_line):
        return Line( self.length + another_line.length )
 
l1 = Line(4)
# print(c1.getlength())
 
# l2 = Line(5)
# print(c2.getlength())
 
# l3 = c1 + c2 
# print(c3.getlength())

# # - Use to pritn custom message
# print(l1)

# ===================================================================================================================
# - if class `C` is inherited from `A`, `B` both and `A`, `B` classes have a method `hello` then when you call `hello` 
# - method of `C` class, which one will be called and why?
#   `class C(A, B) <- class definition
#    c = C(); c.hello() <- will this be a `hello` of A class or B class?`
# ===================================================================================================================

# class A:

#   def hello(self):
#     print("this is class A")

# class B:

#   def hello(self):
#     print("this is class B")

# class C(A,B):
#   pass


# obj = C()
# obj.hello() #This will print hello of class A

# ===================================================================================================================
# - how to declare private methods in a class?
# ===================================================================================================================

# class A:

#   def _hello(self):        #Use __ double underscore to declare private methods ina class
#     print("this is class A")

#   def abc(self):
#     self._hello()
# obj = A()
# obj.abc() 

# ===================================================================================================================
# - a python class can have variables like `_var1` and `__var2` (single underscor and double underscore) what kind of
# - methods are they and how to use / update them?
# ===================================================================================================================

# class A:
#  __count = 0  # single underscore and double underscore are used to declare private member
#  def set_count(self):
#     self.__count += 1; 
#  def get_count(self):
#     return self.__count
# obj = A()
# obj.set_count()
# print(obj.get_count()) 

# ===================================================================================================================
# - how to import a class from other script?
# - how to import a method from other script?
# ===================================================================================================================

#from test import index  #It is not working
#from index import Sum   # Working
# obj = Sum()
# obj.add(1,2)