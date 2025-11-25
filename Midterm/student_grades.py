#Task 1.1
student_names = []
grades = []

def add_student(name, grade):
    student_names.append(name)
    grades.append(grade)
    print(f"Added {name} with grade {grade}")

def calculate_avg_grade():
    sum = 0
    for grade in grades:
        sum += grade
    avg = sum/len(grades)
    print(f"Average Grade:{avg}")

def highest_grade():
    highest = max(grades)
    print(f"Highest Grade:{highest}")

def display_info():
    print("Student Grades:")
    for i in range(len(student_names)):
        name = student_names[i]
        grade = grades[i]
        print(f"{name}:{grade}")

add_student("Alice", 85)
add_student("Bob", 92)
add_student("Charlie", 78)
print("")
display_info()
print("")
calculate_avg_grade()
highest_grade()

#Task 1.2

numbers = [5,2,8,1,9,3]
numbers = sorted(numbers)
print(f"Sorted list:{numbers}")
print("")
sum = sum(numbers)
print(f"Sum:{sum}")
print("")
avg = sum/len(numbers)
print(f"Average:{avg}")
minimum = min(numbers)
maximum = max(numbers)
print(f"Minimum Value:{minimum}")
print(f"Maximum Value:{maximum}")
print("")
list_length = len(numbers)
print(f"List length:{list_length}")