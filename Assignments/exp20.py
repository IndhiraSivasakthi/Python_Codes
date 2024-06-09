def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    symmetric_difference = set1 ^ set2
    return union, intersection, difference, symmetric_difference

input1 = input("Enter elements of first set separated by spaces: ")
input2 = input("Enter elements of second set separated by spaces: ")
set1 = set(map(int, input1.split()))
set2 = set(map(int, input2.split()))

union, intersection, difference, symmetric_difference = set_operations(set1, set2)

print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print("Symmetric Difference:", symmetric_difference)
