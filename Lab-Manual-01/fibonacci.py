num_terms =  int(input("Enter the number of terms: "))
first = 0
second = 1

if num_terms <= 0:
    print("Please enter a positive number: ")
elif num_terms == 1:
    print("Fibonacci series: ", first)
else:
    print("Fibonacci series : ",first, second, end=" ")

for num in range(2, num_terms):
    next_term = first + second
    print(next_term, end=" ")
    first = second
    second = next_term