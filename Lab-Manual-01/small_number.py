AllNumbers = [10, 0, 20, 40, 2, -1]

smallest = AllNumbers[0]

for num in AllNumbers:
    if num < smallest:
        smallest = num

print("This Smallest Number is : ", smallest)