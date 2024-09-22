number = int(input("Enter a number to see its multiplication table: "))

multiplied_number = 0

print(f"Multiplication table for {number}:")

for i in range(1, 11):
    multiplied_number += number  # Increment the product by the user's number
    print(f"{number} * {i} = {multiplied_number}")