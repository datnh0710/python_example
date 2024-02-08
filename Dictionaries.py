#Python Dictionaries
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# Dictionary Items
#Dictionary items are ordered, changeable, and does not allow duplicates
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Changeable
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

#Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Dictionary Length To determine how many items a dictionary has, use the len() function
print(len(thisdict))

#Dictionary Items - Data Types / The values in dictionary items can be of any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#Access Dictionary Items
#You can access the items of a dictionary by referring to its key name, inside square brackets
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#There is also a method called get() that will give you the same result
x = thisdict.get("model")

#The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
#The list of the keys is a view of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the keys list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#Get Values
#The values() method will return a list of all the values in the dictionary
x = thisdict.values()
#The list of the values is a view of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the values list
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Get Items
#The items() method will return each item in a dictionary, as tuples in a list
#Get a list of the key:value pairs
x = thisdict.items()
#The returned list is a view of the items of the dictionary,
#  meaning that any changes done to the dictionary will be reflected in the items list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Check if Key Exists
#To determine if a specified key is present in a dictionary use the "in" keyword
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
      print("Fuck No")

#Change Dictionary Items
#You can change the value of a specific item by referring to its key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#Update Dictionary
#The update() method will update the dictionary with the items from the given argument
#The argument must be a dictionary, or an iterable object with key:value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#Add Dictionary Items
#Adding Items
#Adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#Update Dictionary
#The update() method will update the dictionary with the items from a given argument.
# If the item does not exist, the item will be added
#The argument must be a dictionary, or an iterable object with key:value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#Remove Dictionary Items
#Removing Items

#The pop() method removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#The popitem() method removes the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#The del keyword can also delete the dictionary completely
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Loop Dictionaries
#Loop Through a Dictionary
#You can loop through a dictionary by using a for loop
#When looping through a dictionary, the return value are the keys of the dictionary, 
# but there are methods to return the values as well.

for x in thisdict:
  print(x) #return key of the dictionary

for x in thisdict:
  print(thisdict[x]) # return value of the dictionary   

#You can also use the values() method to return values of a dictionary
for x in thisdict.values():
  print(x)

#You can use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
  print(x)

#Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
  print(x, y)

#Copy Dictionaries
#You cannot copy a dictionary simply by typing dict2 = dict1, 
#because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2
#There are ways to make a copy, one way is to use the built-in Dictionary method copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#Another way to make a copy is to use the built-in function dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


#Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#if you want to add three dictionaries into a new dictionary:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


