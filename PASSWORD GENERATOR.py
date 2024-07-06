import random
import string
def password_generator():
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ")
    use_numbers = input("Include numbers? (y/n): ")
    use_special_chars = input("Include special characters? (y/n): ")

    chars = string.ascii_lowercase
    if use_uppercase.lower() == 'y':
        chars += string.ascii_uppercase
    if use_numbers.lower() == 'y':
        chars += string.digits
    if use_special_chars.lower() == 'y':
        chars += string.punctuation

    password = ''.join(random.choice(chars)
    for _ in range(length))
    print(f"Generated Password: {password}")

password_generator()
    