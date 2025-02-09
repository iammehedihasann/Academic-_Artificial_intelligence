from fontTools.misc.cython import returns

def common_element(list1, list2):
    return list(set(list1) & set(list2))
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

matching_element = common_element(list1, list2)
print("First number element are: ",list1 )
print("Second number element are: ", list2)
print("Common element between sets are: ", matching_element)