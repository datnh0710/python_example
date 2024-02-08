#To make sure a string will display as expected, we can format the result with the format() method.

#String format()
#The format() method allows you to format selected parts of a string
#To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#You can add parameters inside the curly brackets to specify how to convert the value
txt = "The price is {:.2f} dollars"
print(txt.format(price))