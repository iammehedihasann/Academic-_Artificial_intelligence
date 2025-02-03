
numbers = [10, 25, 5, 40, 15, 2, 30]

highest = second_highest = float('-inf')

for num in numbers:
    if num > highest:
        second_highest = highest
        highest = num
    elif num > second_highest and num != highest:
        second_highest = num


if second_highest == float('-inf'):
    print("There is no second highest number.")
else:
    print("The second highest number is:", second_highest)
