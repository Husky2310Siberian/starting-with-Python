# Generate a random password of a specified length.

import secrets
import string

def generate_secure_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase + '-_'
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

password_length = int(input("Password length: "))
password_generated = generate_secure_password(password_length)

print(f"generated password is {password_generated}")
