#set collection
#Sets are used to store multiple items in a single variable.
#A set is a collection which is both unordered and unindexed.
#Set items are unordered, unchangeable, and do not allow duplicate values.

myset = {"apple", "banana", "cherry"}
print(myset)

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}

#sets are defined as objects with the data type 'set'
myset = {"apple", "banana", "cherry"}
print(type(myset))
#Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#Check if "banana" is present in the set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") #Add an item to a set, using the add() method
print(thisset)
#Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #To add items from another set into the current set, use the update() method
print(thisset)
#Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist) #The object in the update() method does not have to be a set,
#it can be any iterable object (tuples, lists, dictionaries etc.).
print(thisset)
#Remove Item To remove an item in a set, use the remove(), or the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #If the item to remove does not exist, remove() will raise an error.
thisset.discard("banana") #If the item to remove does not exist, discard() will NOT raise an error.
#You can also use the pop() method to remove an item, but this method will remove the last item. 
# Remember that sets are unordered, so you will not know what item that gets removed.
x = thisset.pop()
print(x)
print(thisset)
#The clear() method empties the set
thisset.clear()
#The del keyword will delete the set completely
del thisset

#Loop Items You can loop through the set items by using a for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Join Two Sets
#You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another
#Both union() and update() will exclude any duplicate items.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Keep ONLY the Duplicates
#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

z = x.intersection(y) #The intersection() method will return a new set, that only contains the items that are present in both sets.
print(z)

#Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
#symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets
z = x.symmetric_difference(y)
print(x)