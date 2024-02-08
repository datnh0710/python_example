#Modules
#To create a module just save the code you want in a file with the file extension .py
import mymodule

mymodule.greeting("datnguyen")

#Variables in Module

a = mymodule.person1["age"]
print(a)

#Re-naming a Module
#You can create an alias when you import a module, by using the "as" keyword

import mymodule as mx

a = mx.person1["age"]
print(a)

#Using the dir() Function
#There is a built-in function to list all the function names (or variable names) in a module. The dir() function
import platform

x = dir(platform) #The dir() function can be used on all modules, also the ones you create yourself.
print(x) 

#Import From Module
#You can choose to import only parts from a module, by using the "from" keyword
from mymodule import person1

print (person1["age"]) #When importing using the from keyword, 
#do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
