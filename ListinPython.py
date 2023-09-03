# here we learn how to fizzle a data
# into a list

countries = ['United Kingdom', 'Ghana', 'Autralia', 'Russia']
print(countries[2][1])

# to get from a particular number to
# the end you use a colon with the
# index number used during print out

print(countries[1:])

# to know the data type in python we use
# type as a function with the variable

print(type(countries))

# To change the value of one of the
# country to another name or value
# we use the following

countries[0] = 'United States'
countries[3] = 'Canada'
print(countries[2])

group = 'all milk'

food = list(('rice', 'beans', 'soup', group))
print(type(food[3]))

# Using list instead of the square bracket is called
# The list 'constructor'. The list constructor does
# practically the same thing as using a square bracket