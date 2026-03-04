# Diamond Pattern using Nested Loops Only

# Input validation for positive integer
rows = int(input("Enter number of rows for upper half: "))

if rows <= 0:
    print("Please enter a positive integer.")
else:

    # -------- Upper Half --------
    for i in range(1, rows + 1):

        # Print leading spaces
        for space in range(rows - i):
            print(" ", end="")

        # Print stars
        for star in range(2 * i - 1):
            print("*", end="")

        # Move to next line
        print()

    # -------- Lower Half --------
    for i in range(rows - 1, 0, -1):

        # Print leading spaces
        for space in range(rows - i):
            print(" ", end="")

        # Print stars
        for star in range(2 * i - 1):
            print("*", end="")

        # Move to next line
        print()