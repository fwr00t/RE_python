import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to the password generator!")

while True:
    length_input = input("How long would you like your password to be? ")

    try:
        length = int(length_input)
        if length <= 0:
            print("Error: Password length should be a positive number.")
            continue
    except ValueError:
        print("Error: Invalid input. Please enter a positive number for password length.")
        continue

    password = generate_password(length)

    print("\nYour password is:", password)
    print("The length of your password is:", len(password))

    while True:
        choice = input("Would you like to generate another password? (yes/no): ").lower()

        if choice == "yes" or choice == "y":
            break
        elif choice == "no" or choice == "n":
            print("Thank you for using this program!")
            exit()
        else:
            print("Error: Please enter 'yes' or 'no'.")
