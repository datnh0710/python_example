#Creating a Function
#In Python a function is defined using the def keyword
def my_function():
  print("Hello from a function")

#Calling a Function
#To call a function, use the function name followed by parenthesis
def my_function():
  print("Hello from a function")

my_function()

#Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function,
#add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Keyword Arguments
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#rbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function,
#  add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Default Parameter Value
#The following example shows how to use a default parameter value.
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#Passing a List as an Argument
#You can send any data types of argument to a function (string, number, list, dictionary etc.), 
#and it will be treated as the same data type inside the function.
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


#Return Values
# To let a function return a value, use the return statement
def my_function(x):
  return 5 * x
print(my_function(3))

#The pass Statement
#function definitions cannot be empty, but if you for some reason have a function definition with no content,
#  put in the pass statement to avoid getting an error.
def myfunction():
  pass

#Recursion
#Python also accepts function recursion, which means a defined function can call itself.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
