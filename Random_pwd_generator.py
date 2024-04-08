import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage:
password_length = 12  # You can adjust the length as per your requirement
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
