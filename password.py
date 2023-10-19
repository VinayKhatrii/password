import random
import string

capitalLetters = string.ascii_uppercase
smallLetters = string.ascii_lowercase
numbers = string.digits
specialChar = "!@#$%^&?><|_-"

#You can change password length anytime
password_length = 18 

def generate_password():

    essential = [
        random.choice(smallLetters),
        random.choice(specialChar),
        random.choice(capitalLetters),
        random.choice(numbers)
    ]

    random_characters = [
        random.choice(random.choice([smallLetters, specialChar, capitalLetters, numbers]))
        for _ in range(password_length - len(essential))
    ]

    password_characters = essential + random_characters
    random.shuffle(password_characters)

    password = ''.join(password_characters)
    
    return password

try:
    numOfPass = int(input("How many passwords?: "))
    print()
    
    with open("password.txt", "a") as f:
        for _ in range(numOfPass):
            password = generate_password()
            print(password)
            f.write(password + "\n")
    
    print(f"\nAbove are your {numOfPass} passwords")
    
except ValueError:
    print("Enter a valid number of passwords.")
