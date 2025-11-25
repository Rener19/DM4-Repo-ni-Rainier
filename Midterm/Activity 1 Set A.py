#Rainier Justin Aquino
#SET A

def calculate_area(length, width):
    return length * width

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}"

def find_max(*args):
    max = 0
    for arg in args:
        if arg > max:
            max = arg
    return max

def create_user_profile(first_name, last_name, **kwargs):
    dict = {"first_name":first_name, "last_name":last_name}
    for key, value in kwargs.items():
        dict[key] = value
    return dict

print("1:")
print(calculate_area(10,5))
print("\n2:")
print(greet_user("Kurt Russel", "Good morning"))
print("\n3:")
print(find_max(5,3,2,1,3,2))
print("\n4:")
print(create_user_profile("Kurt", "Russel", city="Santiago", sport="volleyball", characteristics="matigas"))
