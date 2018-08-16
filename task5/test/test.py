
# Import classes from your brand new package
import sys
sys.path.insert(0, '/home/ebryx/Desktop/python/python-session/task5/Animals')
from mammals import Mammals
from birds import Birds
# import sys  
# # sys.path.append(pathToFolderContainingScripts)  
# # from scriptName import functionName 

# print(sys.path) 
# Create an object of Mammals class & call a method of it
myMammal = Mammals()
myMammal.printMembers()
 
# Create an object of Birds class & call a method of it
myBird = Birds()
myBird.printMembers()