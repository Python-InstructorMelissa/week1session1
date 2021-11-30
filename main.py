# console.log("Hello World")
# print("Hello World")
"""
This
 is
  a multi line comment
"""
"""
var y = "Whats up class?"
y = "hey there"
var z = "Whats cooking?"
console.log(y+x)
"""

x = "Whats up class? "
y = "Whats cooking?"
# print(x+y)


# Needs to have a comma
# print("Line 20: My question is:", x, "main.py")
# this uses the + instead but does not give space
# print("My Question is:" + y + x)
# This is f string formatting where no , or + is required unless for the sentence
# print(f"My question is {x} {y}")

#  Tuples, Lists, Dictionaries JS vs Python 
# Tuples and Lists are similar to Arrays in JS however Tuples are immutable (can not change) where Lists (and arrays) are mutable and can change
dog = ("Bear", "Abby", "Lucy", "Roxy", "Copper") # Tuple
dogs = ["Bear", "Abby", "Lucy", "Roxy", "Copper"] # List
# print("printing Tuple: ", dog)
# print("printing list: ", dogs)

# print("Just Lucy: ", dog[2])
# print("Just Lucy: ", dogs[2])

# dog.pop()
# dogs.pop()
# print("printing list: ", dogs)

copper = {'name': 'Copper', 'breed': 'Beagle', 'age': '9 months'} # Dictionary
# print(copper)
# print(copper['name'])
copper['weight'] = '24lbs'
copper['color'] = ['brown', 'black', 'white']
# print(copper)
# print(copper['color'])
name = copper['name']
age = copper['age']

# print(f"{name} is {age} years old")


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

for x in range(10, 0, -2): # 1st number = starting 2nd number = stop at 3rd number = increase by
    print(x)