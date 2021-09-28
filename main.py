# JS version = console.log("Hello World")
# print("Hello World")

# this is a single line comment
"""
This is
a multiline
comment
"""

""" JS version = 
var x = "Welcome to Python"
var y = "I will be your instructor"
console.log(x+y)
"""

x = "Welcome to Python"
y = "I will be your instructor"
# print(x+y)

#  Tuples, Lists, Dictionaries JS vs Python 
# Tuples and Lists are similar to Arrays in JS however Tuples are immutable (can not change) where Lists (and arrays) are mutable and can change
dog = ("Bear", "Abby", "Lucy", "Roxy", "Copper") # Tuple
dogs = ["Bear", "Abby", "Lucy", "Roxy", "Copper"] # List
# print(dog)
# print(dogs)

# print(dog[1])
# print(dogs[1])
# dog.pop()
# print(dog)
dogs.pop()
# print(dogs)
copper = {'name': 'Copper', 'breed': 'Beagle', 'age': '6 months'} # Dictionary
# print(copper)
# print(copper['name'])
copper['weight'] = '24lbs'
# print(copper)
copper['color'] = ['brown', 'black', 'white']
# print(copper)
c = copper.pop('color')
# print(c)
# print(copper)


# Printing and combining strings 3 methods
firstName = 'Melissa'
lastName = 'Longenberger'
age = 42
city = 'Berwick'
state = 'PA'

# print("I live in", city, state, "my name is", firstName, lastName, "and I am", age, "years old.")
# print("I live in" + city + state + "my name is" + firstName + lastName + "and I am" + age + "years old.")
# print("I live in" + city + state + "my name is" + firstName + lastName)
# print("I live in " + city +  " " + state + " " + "my name is " + firstName + " " + lastName)

# print(f"I live in {city} {state} my name is {firstName} {lastName} and I am {age} years old")


x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")

# for(let x = 0; x < 10; x+=2) {
#     console.log(x)
# }

for x in range(0, 10, 2): # 1st number = starting 2nd number = stop at 3rd number = increase by
    print(x)
