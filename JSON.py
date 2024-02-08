#JSON
#JSON is a syntax for storing and exchanging data.
#JSON is text, written with JavaScript object notation.
#JSON in Python
#Python has a built-in package called json, which can be used to work with JSON data.
import json


#Parse JSON - Convert from JSON to Python
#If you have a JSON string, you can parse it by using the json.loads() method

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#Convert from Python to JSON
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#Format the Result
#Use the indent parameter to define the numbers of indents
json.dumps(x, indent=4)

#You can also define the separators, default value is (", ", ": "), 
#which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
json.dumps(x, indent=4, separators=(". ", " = "))

#Order the Result
#The json.dumps() method has parameters to order the keys in the result
json.dumps(x, indent=4, sort_keys=True)