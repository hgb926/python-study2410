import math

print("Hello World")

name = "Alice"
age = 30
height = 4.1
is_student = True
fruits = ["apple", "orange", "pear"]
print(fruits[0])

point = (10, 20)
print(point[1])

person = {"name": "Alice", "age": 30, "height": 4.1}
print(person["name"])

if age < 19:
    print("어린이")
elif age < 65:
    print("성인")
else:
    print("노인")

for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 2

def greet(name):
    return f"Hello {name}!"
print(greet("Alice"))

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} say woof!"
my_dog = Dog("Buddy")
print(my_dog.bark())


print(math.sqrt(16))


