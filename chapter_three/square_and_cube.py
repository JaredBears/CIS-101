numList = [1,3,5,7,9]

print(f'{"":>10} {"Square":>10} {"Cube":>10}')
for i in range(len(numList)):
    print(f'{numList[i]:>10} {numList[i]**2:>10} {numList[i]**3:>10}')