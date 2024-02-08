#Python Arrays
#Python does not have built-in support for Arrays, but Python Lists can be used instead.
#This page shows you how to use LISTS as ARRAYS, however,
#to work with arrays in Python you will have to import a library, like the NumPy library.

#for example:
cars = ["Ford", "Volvo", "BMW"]

#Access the Elements of an Array
x = cars[0]
cars[0] = "Toyota"

#The Length of an Array
#Use the len() method to return the length of an array
#The length of an array is always one more than the highest array index.
x = len(cars)

#Looping Array Elements
for x in cars: #You can use the for in loop to loop through all the elements of an array
  print(x)

#Adding Array Elements
cars.append("Honda") #You can use the append() method to add an element to an array

#Removing Array Elements
cars.pop(1) #You can use the pop() method to remove an element from the array
#You can also use the remove() method to remove an element from the array
cars.remove("Volvo") #The list's remove() method only removes the first occurrence of the specified value.