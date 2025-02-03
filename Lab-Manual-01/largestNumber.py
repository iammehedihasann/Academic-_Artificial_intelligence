def find_largest(num1, num2 ):
    if num1 > num2:
        return num1
    else:
        return num2

number1 = float(input("Enter the First number: "))
number2 = float(input("Enter the second number: "))

largest = find_largest(number1, number2)
print("The largest number is: ", largest)