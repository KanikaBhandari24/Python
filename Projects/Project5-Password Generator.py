import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the MyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# EASY PASSWORD CREATION
password = ""
for char in range(1, nr_letters+1):
    # 1 to 4
    random_char=random.choice(letters)
    password += random_char

for char in range(1, nr_numbers+1):
    random_char=random.choice(numbers)
    password += random_char

for char in range(1, nr_symbols+1):
    random_char=random.choice(symbols)
    password += random_char

print(password)

#HARD PASSWORD CREATION
# password = []
# for char in range(1, nr_letters+1):
#     # random_char=random.choice(letters)
#     # password.append(random_char)

#     password.append(random.choice(letters))

# for char in range(1, nr_numbers+1):
#     # random_char=random.choice(numbers)
#     # password += random_char

#     password += (random.choice(numbers))

# for char in range(1, nr_symbols+1):
#     # random_char=random.choice(symbols)
#     # password += random_char

#     password += (random.choice(symbols))

# print(password)
# random.shuffle(password)    #shuffle updates the existing list
# print(password)

# pw= ""
# for char in pw:
#     pw += char

# print(f"Your password is - {pw}")




