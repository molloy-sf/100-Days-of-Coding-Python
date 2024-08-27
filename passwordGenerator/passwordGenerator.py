# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rand_password = []
for letter in range(0, nr_letters):
    rand_password += letters[random.randint(0, 51)]

for num in range(0, nr_numbers):
    rand_password += numbers[random.randint(0, 9)]

for sym in range(0, nr_symbols):
    rand_password += symbols[random.randint(0, 8)]

new_pass = []
old_list = len(rand_password)
char = None

for count in range(0, old_list):
    if len(rand_password) > 0:
        char = random.randint(0, old_list - 1)
        new_pass += rand_password[char]
        del rand_password[char]
        old_list = len(rand_password)

final_pass = ""
for item in new_pass:
    final_pass += item

print(f"\nfinal password = {final_pass}")