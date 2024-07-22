import random
import string

def generate_password(length=12):
    # Length Minimum for Password 
    if length < 8:
        raise ValueError("Password Length Should Be At Least 8 Characters.")

    # Characters to include in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has at least one upper, lower, digit, and special character
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter the desired password length (minimum 8): "))
    password = generate_password(length)

   #Outputs the final code
    print(f"Generated Secure Password: {password}")
