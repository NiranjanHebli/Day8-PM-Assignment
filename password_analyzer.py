import random
import string


def analyze_password(password):
    """
    Analyzes password strength based on:
    - Length criteria
    - Character type presence
    - No more than 2 consecutive repeated characters
    Returns: (score, missing_criteria_list)
    """

    score = 0
    missing = []

    length = len(password)

    # Longer passwords get more points
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        missing.append("too short")

    # Flags to track character types
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    no_repeat = True

    special_chars = "!@#$%^&*"
    repeat_count = 1

    # Using a for loop to inspect each character
    for i in range(len(password)):
        ch = password[i]

        # Check character type
        if 'A' <= ch <= 'Z':
            has_upper = True
        elif 'a' <= ch <= 'z':
            has_lower = True
        elif '0' <= ch <= '9':
            has_digit = True
        elif ch in special_chars:
            has_special = True

        # Check for more than 2 repeated characters in a row
        if i > 0 and password[i] == password[i - 1]:
            repeat_count += 1
            if repeat_count > 2:
                no_repeat = False
        else:
            repeat_count = 1

    if has_upper:
        score += 1
    else:
        missing.append("uppercase")

    if has_lower:
        score += 1
    else:
        missing.append("lowercase")

    if has_digit:
        score += 1
    else:
        missing.append("digit")

    if has_special:
        score += 1
    else:
        missing.append("special char")

    if no_repeat:
        score += 1
    else:
        missing.append("repeated characters")

    return score, missing


def strength_rating(score):
    """
    Converts numeric score into human-readable rating.
    """
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score <= 6:
        return "Strong"
    else:
        return "Very Strong"


def generate_password(length):
    """
    Generates a random password using:
    - Uppercase + lowercase letters
    - Digits
    - Punctuation characters
    """

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    # Use for loop to build password character by character
    for _ in range(length):
        password += random.choice(characters)

    return password


# Using while True to simulate do-while behavior
# Program runs at least once and repeats until user exits
while True:

    print("\nPassword Analyzer & Generator")
    print("1. Analyze Password")
    print("2. Generate Secure Password")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":

        # Keep asking until password strength is at least 5
        while True:
            user_password = input("Enter password: ")

            score, missing = analyze_password(user_password)
            rating = strength_rating(score)

            print(f">> Strength: {score}/7 ({rating})")

            if missing:
                print(">> Missing:", ", ".join(missing))

            if score >= 5:
                print(">> Password accepted!")
                break
            else:
                print(">> Try again...\n")

    elif choice == "2":

        length = int(input("Enter desired password length: "))
        generated = generate_password(length)

        score, missing = analyze_password(generated)
        rating = strength_rating(score)

        print("\nGenerated Password:", generated)
        print(f"Strength: {score}/7 ({rating})")

        if missing:
            print("Missing criteria:", ", ".join(missing))
        input("Press Enter to return to menu...")

    elif choice == "3":
        print("Exiting program. Stay secure! 🔐")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")