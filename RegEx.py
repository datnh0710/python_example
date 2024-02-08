#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.

#RegEx Module
import re

#RegEx in Python
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

#The findall() Function
#The findall() function returns a list containing all matches.
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#The search() Function
#The search() function searches the string for a match, and returns a Match object if there is a match
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#The split() Function
#The split() function returns a list where the string has been split at each match
#You can control the number of occurrences by specifying the maxsplit parameter
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
x = re.split("\s", txt, 1)
print(x)

#The sub() Function
#The sub() function replaces the matches with the text of your choice
#You can control the number of replacements by specifying the count parameter
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
x = re.sub("\s", "9", txt, 2)
print(x)

#Match Object
#A Match Object is an object containing information about the search and the result.
#If there is no match, the value None will be returned, instead of the Match Object.
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
#The Match object has properties and methods used to retrieve information about the search, and the result:
""".span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match"""

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
