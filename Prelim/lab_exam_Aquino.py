#Rainier Justin H. Aquino BSCS 3-1 Lab Exam

import sys

#Task 1
print("Task 1:")
def grade_student(score):
    if 100 >= score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(grade_student(95))
print(grade_student(75))
print(grade_student(50))
print("\n")

#Task 2
print("Task 2:")
def process_string(str):

    vowels = "aeiou"
    vowel_count = 0
    for letter in str:
        if letter in vowels:
            vowel_count += 1

    new_str = (f"Uppercase:{str.upper()}\n"
               f"Reversed:{str[::-1]}\n"
               f"No. of Vowels: {vowel_count}")
    return new_str

print(process_string("Python Programming"))
print("\n")

#Task 3
print("Task 3:")
num_list = []
for i in range(5):
    num = int(input(f"Input num {i+1}: "))
    num_list.append(num)

sum = 0
for num in num_list:
    sum += num

average = sum/len(num_list)

print(f"List: {num_list}: ")
print(f"Sum: {sum}")
print(f"Average: {average}")
print("\n")

#Task 4
print("Task 4:")

if len(sys.argv) > 1:
    file = open(f"{sys.argv[1]}", "r")
    content = file.read()
    print(content)
    file.close()
else:
    print("No file provided for task 4")
print("\n")

#Task 5
print("Task 5:")

def create_profile(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")

create_profile(name="Alice", age=25, city="Tokyo")