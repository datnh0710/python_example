#Classes and Objects
#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects

#Create a Class

class MyClass: #To create a class, use the keyword class
  x = 5

#Create Object
p1 = MyClass() #we can use the class named MyClass to create objects
print(p1.x)

#The __init__() Function
#he examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#To understand the meaning of classes we have to understand the built-in __init__() function.
#All classes have a function called __init__(), 
#which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties,
#or other operations that are necessary to do when the object is being created

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36) #The __init__() function is called automatically every time the class is being used to create a new object.

print(p1.name)
print(p1.age)

#Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#The self Parameter
#The self parameter is a reference to the current instance of the class, 
#and is used to access variables that belongs to the class.
class Person:
  def __init__(mysillyobject, name, age):#Self does not have to be named self , 
      #you can call it whatever you like, but it has to be the first parameter of any function in the class
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Modify Object Properties
p1.age = 40 #Set the age of p1 to 40

#Delete Object Properties
del p1.age #You can delete properties on objects by using the del keyword

#Delete Objects
del p1 #You can delete objects by using the del keyword

#The pass Statement
class Person: # class definitions cannot be empty, 
             #but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
  pass