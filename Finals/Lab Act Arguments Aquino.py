#Part 1

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} and its name is {pet_name}")

print("Part 1")
describe_pet("Dog", "Kurt")
describe_pet("Cat", "Russel")
describe_pet("Horse", "Vincent")
print("")

#Part 2

print("Part 2")
describe_pet("Bunny", "Bugs")
describe_pet(pet_name="Chris Johnson", animal_type="Turtle")
print("")

#Part 3

print("Part 3")
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} and its name is {pet_name}")

describe_pet("Brownie")
describe_pet("Nugget","Chicken")
print("")

#Part 4

print("Part 4")
def order_drink(drink, size="medium", iced = False):
    print(f"Your order: {size} {"iced" if iced else "no ice"} {drink}")

order_drink("Matcha")
order_drink("hot chocolate", "large", False)
order_drink("milk tea", "small", True)

#Part 5

print("Part 5")
def compute(operation, num1, num2=1):
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operation"

print(compute("add",5,10))
print(compute("multiply", num1=3,num2=4))
print(compute("subtract",20))
print(compute("maynos",69,67))