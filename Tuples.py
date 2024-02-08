#Tuples

#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1]
#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
thistuple = ("apple", "banana", "cherry") #creating tuple
print(thistuple)

#To determine how many items a tuple has, use the len() function
print(len(thistuple))
#Create Tuple With One Item
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
histuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple") #str class
print(type(thistuple))

#Tuple items can be of any data type
tuple1 = ("abc", 34, True, 40, "male")

#The tuple() Constructor - It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Access Tuple Items
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1]) #positive index - start beginning the tuple 
print(thistuple[-1]) # negative index - start ending the tuple
print(thistuple[2:5]) # The search will start at index 2 (included) and end at index 5 (not included).
print(thistuple[:4]) #returns the items from the beginning to, but NOT included, "kiwi"
print(thistuple[-4:-1]) #Range of Negative Indexes
#Check if Item Exists
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Update Tuples - Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

#Add Items
#1. Convert into a list: 
# Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#2. Add tuple to a tuple. You are allowed to add tuples to tuples, 
# so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#Tuples are unchangeable, so you cannot remove items from it,
#  but you can use the same workaround as we used for changing and adding tuple items:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#The del keyword can delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) 

#Unpack Tuples
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple
fruits = ("apple", "banana", "cherry") #packing a tuple

#in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#Using Asterisk *
#If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Loop Through the Index Numbers - Use the range() and len() functions to create a suitable iterable.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Using a While Loop
#Use the len() function to determine the length of the tuple,
#then start at 0 and loop your way through the tuple items by refering to their indexes.
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2