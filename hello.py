import random


"""
this is comment
"""
print("hello boy")

def myfunc():
    print("my function!!!")

myfunc()

#ramdom function
print("Ramdom: ")
print(random.randrange(1,10))
x = str("hello boy") #string
print(x)
print(x[1])
print(type(x))
x = 20 #int
print(x)
print(type(x))
x = 20.5 # float
print(x)
print(type(x))
x = 1j #complex
print(x)
print(type(x))
x = ['a','b','c'] # list
print(x)
print(type(x))
x = ('d','e','f') #tuple
print(x)
print(type(x))
x = range(6) #range
print(x)
print(type(x))
x = {"name": "Dat", "age": 28} #dict
print(x)
print(type(x))
x = {'g','h','k'} # set
print(x)
print(type(x))
x = frozenset({'apple','banana','cherry'}) #frozenset
print(x)
print(type(x))
x = True # bool
print(x)
print(type(x))
x = b"hello boy" #bytes
print(x)
print(type(x))
x = bytearray(5) #bytearray
print(x)
print(type(x))
x = memoryview(bytes(5)) #memoryview
print(x)
print(type(x))

a,b,c = 'a','b','c'
print(a)
print(b)
print(c)

fruits=["apple","banana","cherry"]
a,b,c = fruits
print(a)
print(b)
print(c)

#using for
s = "i love you so muc"
for x in s:
    print(x)
#lenght of str
print(len(s))

# check any pharse or charater is present in string, use  the keyword "in"
print("love" in s)
if "love" in s:
    print("Yes, Love is present.")

# check any pharse or charater is not present in string, use  the keyword "not in"
print("hurt" in s)
if "hurt" not in s:
    print("Yes, Hurt is not  present.")

#Slicing
b = "Hello, World!"
print(b[2:5])#Get the characters from position 2 to position 5 (not included)

#Slice From the Start
b = "Hello, World!"
print(b[:5]) #Get the characters from the start to position 5 (not included)

#Slice To the End
b = "Hello, World!"
print(b[2:]) #Get the characters from position 2, and all the way to the end

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

#The upper() method returns the string in upper case
a = "Hello, World!"
print(a.upper())

#The lower() method returns the string in lower case:
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:
print(a.strip())

#The replace() method replaces a string with another string:
print(a.replace("H", "J"))

#The split() method returns a list where the text between the specified separator becomes the list items.
print(a.split(",")) # returns ['Hello', ' World!']

#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Exponentiation
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2

x = 15
y = 2

print(x // y)#the floor division // rounds the result down to the nearest whole number

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.

# newlist = [expression for item in iterable if condition == True]
#The return value is a new list, leaving the old list unchanged.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

#List Comprehension with condition
newlist = [x for x in fruits if "a" in x]
#With no if statement
newlist = [x for x in fruits]
#Iterable
#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]
print(newlist)
#The expression 
newlist = [x.upper() for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
#To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
#Customize Sort Function
#You can also customize your own function by using the keyword argument key = function.
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#uckily we can use built-in functions as key functions when sorting a list.
#So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#What if you want to reverse the order of a list, regardless of the alphabet?
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#You cannot copy a list simply by typing list2 = list1, 
#because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#Make a copy of a list with the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
for x in list2:
  list1.append(x)
list1.extend(list2)