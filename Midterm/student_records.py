#Task 4.1

import pickle

def save_students_pickle(filename, data):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
    print(f"Saved to {filename}")

def load_students_pickle(filename):
    with open(filename, "rb") as file:
        data = pickle.load(file)
    print(f"Loaded from {filename}")
    return data


def export_students_text(filename, data):
    with open(filename, "w") as file:
        file.write("STUDENT RECORDS\n")

        for student_id, info in data.items():
            file.write(f"ID: {student_id}\n")
            file.write(f"Name: {info['name']}\n")
            file.write(f"Grade: {info['grade']}\n")
            file.write(f"Major: {info['major']}\n")
            file.write("--------------------\n")

    print(f"Exported to {filename}")

students = {
    1: {"name": "Alice", "grade": "A", "major": "Computer Science"},
    2: {"name": "Bob", "grade": "B+", "major": "Mathematics"},
    3: {"name": "Charlie", "grade": "A-", "major": "Engineering"}
}


save_students_pickle("students.pkl", students)

loaded_students = load_students_pickle("students.pkl")
print("\nLoaded Data:", loaded_students)

export_students_text("students.txt", loaded_students)

#Task 4.2

filename = "testing.txt"

with open(filename, "w") as file:
    file.write("Test line 1\n")
    file.write("Test line 2\n")
print(f"Data written to {filename}")

try:
    with open(filename, "r") as file:
        print("\nReading from file:")
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: {filename} not found!")

with open(filename, "a") as file:
    file.write("Test Append line.\n")
print(f"Data appended to {filename}")

try:
    with open(filename, "r") as file:
        print("\nReading after appending:")
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: {filename} not found!")
