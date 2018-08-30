# - Decorator: A function that is used to extend the behaviour of function without modify that function

# #===============================================================================================================
# # - How to use decorator
# #===============================================================================================================
# def decor(func):

# 	def wrap():
# 		print("===============")
# 		func()
# 		print("===============")
# 	return wrap

# @decor
# def greet():
# 	print("hello")


# def wish():
# 	print("bye bye")


# greet()
# d = decor(wish)
# d()
# wish()

# #===============================================================================================================
# # - How to use Regular expression
# #===============================================================================================================
# import re

# #Example no 1: Check email is valid or not

# pattern = r'^\w+@[a-zA-Z_]+\.[a-zA-Z]{2,3}$'
# str = "nazimnaeem@ebryx.com"
# check_email = re.match(pattern,str)
# if check_email:
# 	print("valid email")
# else:
# 	print("Invalid Email")

# #Example no 2: Check Phone no is valid or not

# pattern = r'^[0-9]{4}\-[0-9]{7}$'
# num = "03i2-5650853"
# check_num = re.match(pattern,num)
# if check_num:
# 	print("valid number")
# else:
# 	print("Invalid number")

# #===============================================================================================================
# # - How to use Property
# #===============================================================================================================

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

#     @property
#     def gotmarks(self):
#         return self.name + ' obtained ' + self.marks + ' marks'

#     @gotmarks.setter
#     def gotmarks(self, sentence):
#         name, rand, marks = sentence.split(' ')
#         self.name = name
#         self.marks = marks


# st = Student("Arij", "25")
# print(st.name)
# print(st.marks)
# print(st.gotmarks)
# print("##################")
# st.name = "Nazim"
# print(st.name)
# print(st.gotmarks)
# print("##################")
# st.gotmarks = 'Shahid got 36'
# print(st.gotmarks)
# print(st.name)
# print(st.marks)

# #===============================================================================================================
# # - How to use Generator(yield)
# #===============================================================================================================


# # A simple generator for Fibonacci Numbers
# def fib(limit):
     
#     # Initialize first two Fibonacci Numbers 
#     a, b = 0, 1
 
#     # One by one yield next Fibonacci Number
#     while limit:
#         yield a
#         limit -=1
#         a, b = b, a + b
 		
# print("Using for in loop")
# for result in fib(6): 
#     print(result)