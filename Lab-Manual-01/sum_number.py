
numbers = [ 10, 21, 36, 42, 50, 69, 17, 85, 91, 130]

even_sum = 0
odd_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of the Even numbers: ", even_sum)
print("Sum of the odd Numbers: ",odd_sum)