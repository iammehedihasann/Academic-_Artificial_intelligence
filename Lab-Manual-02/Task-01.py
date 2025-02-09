from collections import Counter
from enum import unique


def Find_Doublicate_number(lst):
    counts = Counter(lst)
    dublicates = [num for num, count in counts.items() if count > 1 ]
    unique_sorted = sorted(set(lst))
    print("Duplicte numbers is : ", dublicates)
    return unique_sorted

numbers = [5, 3, 8, 3, 1, 5, 7, 8, 2]
print("Numbers is :", numbers)
sorted_numbers = Find_Doublicate_number(numbers)
print("Sorted unique numbers is :", sorted_numbers)