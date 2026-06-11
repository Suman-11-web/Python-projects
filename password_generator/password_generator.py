import string
import secrets

def generate_password(length=12):
    """Generates a secure random password."""
    # Define the character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Combine all characters
    all_characters = lowercase + uppercase + digits + symbols
    
    # Ensure the password has at least 8 characters for security
    if length < 8:
        print("Warning: Passwords under 8 characters are generally insecure.")
        length = 8
        
    # Generate the password securely using the secrets module
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Python Password Generator!")
    
    # Get user input for password length
    try:
        user_length = int(input("Enter the desired password length (minimum 8): "))
        generated_password = generate_password(user_length)
        print(f"\nYour generated password is: {generated_password}")
    except ValueError:
        print("Invalid input! Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
