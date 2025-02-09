numbers = [25, 30, 35, 40, 45, 9, 18 ]
total_sum = 0

for num in numbers:
    if num % 3 == 0 and num % 5 != 0:
        total_sum += num

print("The sum of numbers  divisible by 3 but not 5 is :", total_sum)

