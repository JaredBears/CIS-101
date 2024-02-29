'''
Create a program that shows the logic for a program that prompts the user to input an integer that represents cents. The program will then calculate the smallest combination of coins that the user has. For example, 32 cents is 1 quarter, 1 nickel, and 2 pennies 
'''

# Prompt the user to input an integer that represents cents
cents = int(input("Enter the number of cents: "))
# Calculate the number of quarters and remaining cents
quarters, cents = cents // 25, cents % 25
# Calculate the number of dimes and remaining cents
dimes, cents = cents // 10, cents % 10
# Calculate the number of nickels and remaining pennies
nickels, pennies = cents // 5, cents % 5
# Display the smallest combination of coins
print(f'The smallest combination of coins is {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.')