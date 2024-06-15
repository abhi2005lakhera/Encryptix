import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    #the character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensuring the password has at least one letter, one digit, and one special character
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars),
    ]
    
    all_chars = letters + digits + special_chars
    password += random.choices(all_chars, k=length - 3)
    
    # Shuffle the resulting password list to ensure random order
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)

# the desired password length
try:
    password_length = int(input("Enter the desired password length (minimum 4 characters): "))
    generated_password = generate_password(password_length)
    print(f"Generated password: {generated_password}")
except ValueError as e:
    print(f"Error: {e}")