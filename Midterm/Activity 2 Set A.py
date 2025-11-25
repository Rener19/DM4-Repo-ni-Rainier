#Rainier Justin Aquino
#SET A
print("1: ")
full_name = input("Enter full name: ").title().strip()

index = 0
for letter in full_name:
    if letter.isupper() and index!=0:
        break

    index += 1

first_name = full_name[:index]
last_name = full_name[index:]

print(f"first_name: {first_name}")
print(f"last_name: {last_name}")

print("2: ")
filename = f"{first_name.strip().lower()}_{last_name.strip().lower()}_report_20241007.txt"
print(filename)

print("3: ")
def is_valid_password(password):
    has_letter = any(c.isalpha() for c in password)
    has_num = any(c.isdigit() for c in password)

    if len(password) >= 8 and has_letter and has_num:
        return True
    return False


password = input("Input password:")
print(f"Password is valid: {is_valid_password(password)}")

print("4: ")
def reverse_words(sentence):
    words = sentence.split(" ")
    new_sentence = ""

    for i in range(len(words)):
        new_sentence += f"{words[-(i+1)]} "

    return new_sentence

sentence = input("Enter sentence to reverse: ")
print(reverse_words(sentence))
