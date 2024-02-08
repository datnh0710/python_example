#Iterator vs Iterable
#Lists, tuples, dictionaries, and sets are all iterable objects. 
# They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Even strings are iterable objects, and can return an iterator
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))

#Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")
#The for loop actually creates an iterator object and executes the next() method for each loop.
for x in mytuple:
  print(x)

#Create an Iterator
#To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
class Mynumber:
    def __iter__(self):
        self.a =1
        return self
    def __next__(self):
        x= self.a
        self.a +=1
        return x
myclass = Mynumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))

#StopIteration
#To prevent the iteration to go on forever, we can use the StopIteration statement
#In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
class Mynumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<20:
            x = self.a
            self.a+=1
            return x
        else:
            raise StopIteration

myclass = Mynumber()
myiter = iter(myclass)
for x in myiter:
  print(x)