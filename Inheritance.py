#Python Inheritance

#Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()

#Create a Child Class
#Create a class named Student, which will inherit the properties and methods from the Person class
class Student(Person):
  pass #Use the pass keyword when you do not want to add any other properties or methods to the class

x = Student("Mike", "Olsen")
x.printname()


#Add the __init__() Function
#We want to add the __init__() function to the child class (instead of the pass keyword)
class Student(Person):
  def __init__(self, fname, lname):  #The __init__() function is called automatically every time the class is being used to create a new object.
      #When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
      #The child's __init__() function overrides the inheritance of the parent's __init__() function.
      #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
    Person.__init__(self, fname, lname)

#Use the super() Function
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) #By using the super() function, you do not have to use the name of the parent element, 
    #it will automatically inherit the methods and properties from its parent.


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

#Add Methods
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
#If you add a method in the child class with the same name as a function in the parent class,
#  the inheritance of the parent method will be overridden.

