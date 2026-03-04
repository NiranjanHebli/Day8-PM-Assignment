# Diamond Pattern using Nested Loops Only

# Input validation for positive integer
while True:
    rows = int(input("Enter number of rows for upper half: "))
    if rows > 0:
        break
    print("Please enter a positive integer.")

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))
