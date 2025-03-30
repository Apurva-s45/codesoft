# Password Generator Program
import random
import string

def generate_password(length):
    # Combine lowercase, uppercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        # Prompt user for desired password length
        length = int(input("Enter the desired length for your password: "))
        if length <= 0:
            print("Password length must be greater than zero.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number for the password length!")

if __name__ == "__main__":
    main()
