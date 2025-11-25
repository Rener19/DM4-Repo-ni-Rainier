#Task 3.1
students = {}

def add_student(student_id,name,grade,major):
    students[student_id] = {
        'name': name,
        'grade': grade,
        'major': major
    }

def student_info(student_id):
    student_name = students[student_id]["name"]
    student_grade = students[student_id]["grade"]
    student_major = students[student_id]["major"]

    print(f"Student ID: {student_id}")
    print(f"Name: {student_name}")
    print(f"Grade: {student_grade}")
    print(f"Major: {student_major}")

add_student(1,"Rainier","A+", "Computer Science")
add_student(2, "Justin", "C", "Information Technology")
add_student(3, "Chris Johnson", "B+", "Information Systems")

student_info(1)
student_info(2)
student_info(3)

#Task 3.2

text = "Python is a programming language. Python is easy to learn. Python is powerful."

text = text.lower()

for p in ".,!?":
    text = text.replace(p, "")

words = text.split()

word_counter = {}

for word in words:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

sorted_words = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)


print("Sorted word frequencies:")
for word, count in sorted_words:
    print(word, ":", count)


most_common_word = sorted_words[0][0]
most_common_count = sorted_words[0][1]

print("\nMost common word:")
print(most_common_word, "appears", most_common_count, "times")