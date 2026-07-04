import random
import string


# -----------------------------
# Generate Password Function
# -----------------------------
def generate_password(length, choice):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    if choice == 1:
        characters = lowercase

    elif choice == 2:
        characters = lowercase + uppercase

    elif choice == 3:
        characters = lowercase + uppercase + numbers

    elif choice == 4:
        characters = lowercase + uppercase + numbers + symbols

    else:
        return None

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


# -----------------------------
# Main Program
# -----------------------------
print("=" * 45)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 45)

while True:

    try:

        length = int(input("\nEnter Password Length: "))

        if length <= 0:
            print("Length must be greater than 0.")
            continue

        print("\nPassword Complexity")
        print("1. Lowercase Only")
        print("2. Lowercase + Uppercase")
        print("3. Letters + Numbers")
        print("4. Letters + Numbers + Symbols")

        choice = int(input("\nChoose option (1-4): "))

        password = generate_password(length, choice)

        if password is None:
            print("Invalid Choice")
            continue

        print("\nGenerated Password")
        print("-" * 25)
        print(password)
        print("-" * 25)

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != 'y':
            print("\nThank you for using Password Generator.")
            break

    except ValueError:
        print("Please enter valid numbers only.")