import random
import string
def generate_password(length=12):
    # Define the characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print(generate_password())


