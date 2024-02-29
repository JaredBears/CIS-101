COST_PER_VEG = 30
COST_PER_NON_VEG = 25

vegList = []
nonVegList = []

while True:
    friend = input("Enter your friend's name or 'done' to quit: ")
    if friend == 'done':
        break
    while True:
        veg = input(f"Is {friend} a vegetarian? (yes/no): ")
        if veg.lower() == 'yes' or veg.lower() == 'y':
            vegList.append(friend)
            break
        elif veg.lower() == 'no' or veg.lower() == 'n':
            nonVegList.append(friend)
            break
        else:
            print("Please enter 'yes' or 'no'.")
largerList = vegList if len(vegList) > len(nonVegList) else nonVegList
print(f'{"":>15}{"Vegetarians":>15} {"Non-Vegetarians":>15}')

for i in range(len(largerList)):
    if i < len(vegList):
        print(f'{"":>15}{vegList[i]:>15}', end='')
    else:
        print(f'{"":>15}{"":>15}', end='')
    if i < len(nonVegList):
        print(f'{nonVegList[i]:>15}')
    else:
        print(f'{"":>15}')
    print(f'{"Total":>15} {len(vegList):>15} {len(nonVegList):>15}')
    print(f'{"Cost":>15} {len(vegList) * COST_PER_VEG:>15} {len(nonVegList) * COST_PER_NON_VEG:>15}')

print(f'The total number of guests is: {len(vegList) + len(nonVegList)}')
print(f'The total cost for the party is: {len(vegList) * COST_PER_VEG + len(nonVegList) * COST_PER_NON_VEG}')
