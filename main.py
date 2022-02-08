# console.log("Hello World")
# print("Hello World")

""" 
JS version = 
var x = "Welcome to Python"
var y = "I will be your instructor"
console.log(x+y)
"""
x = "Welcome to Python"
y = "I will be your instructor"
# print(x+y)

# print(x,y)

# print(f"{x} {y}")
# print(f"Welcome to Python {y}")
# print("Welcome to Python", y)

food = ("Lasagna", "Pizza", "Chips") # Tuple
foods = ["Lasagna", "Pizza", "Chips"] # List

# print("printing the Tuple: ", food)
# print("printing the list: ", foods)

# food.pop()
foods.pop()
# print("list after pop:", foods)

person = {"firstName": "Melissa", "age": 44, "location": "Berwick, PA"}
# person['name'] = "Jane"
# print("printing the name in the dictionary:", person['name'])
instructor = person['firstName']
age = person['age']
location = person['location']
# print(f"{instructor}, is our instructor and she is {age} years old and lives in {location}")
# print("whole dictionary", person)


x = 55
if x > 10:
    print("bigger than 10")
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")

    # 2 if statements if both are true will print 
    # if and elif only the 1st one that is true will print

# for(let x = 0; x < 10; x+=2) {
#     console.log(x)
# }
for x in range(0, 10, 2): # 1st number = starting 2nd number = stop at 3rd number = increase by
    print("increase by 2:", x)

for x in range(10, 0, -2): # 1st number = starting 2nd number = stop at 3rd number = increase by
    print("decrease by 2:", x)

# function
def test():
    print("this is just a test")

test()

def testing():
    pass