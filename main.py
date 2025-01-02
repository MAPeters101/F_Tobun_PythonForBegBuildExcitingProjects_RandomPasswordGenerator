import random
import string
def generate_password(length=12):
    # Define the characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password2(length=12):
    # Define the characters to include in the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    password = (
        random.choice(uppercase_letters) +
        random.choice(lowercase_letters) +
        random.choice(digits) +
        random.choice(special_characters)
    )
    remaining_length = length - 4

    characters = string.ascii_letters + string.digits + string.punctuation
    password += ''.join(random.choice(characters) for _ in range(remaining_length))
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


print(generate_password())
print(generate_password2())


