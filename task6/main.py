#====================================================================================================================
#									Task 6
#====================================================================================================================

# - How to define abstract class and how to use them

# - What is diamond problem and how to remediate it in python).


#===================================================================================================================
#									Solution
#===================================================================================================================


#===================================================================================================================
# - How to define abstract class and how to use them
#===================================================================================================================
	
# from abc import ABC, abstractmethod
 
 
# class Vechile(ABC):
 
#     def __init__(self, name):
#     	self.name = name
#     	pass

#     @abstractmethod
#     def speed(self):
#         pass

#     @abstractmethod
#     def run(self):
#         pass


# class Suzuki(Vechile):

#     def speed(self):
#         print("%s speed is 150km/h"%(self.name))

#     def run(self):
#         print("%s speed is smoothly" %(self.name))
	        

# car = Suzuki("Suzuki")
# car.speed()
# car.run()


#===================================================================================================================
# - What is diamond problem and how to remediate it in python).
#===================================================================================================================


 
# class Father:
  
# 	def blood_Group(self):
# 		print ("AB+")

# class Mother:

# 	def blood_Group():
# 		print("B+")


# class Child(Father, Mother):  # Function of that class depend upon the order of the class inherit  

# 	def which_Blood_Group(self):
# 		self.blood_Group()



# obj = Child()
# obj.which_Blood_Group()

