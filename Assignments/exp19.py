def is_subset(set1, set2):
    return set1.issubset(set2)


set1 = {1, 2}
set2 = {1, 2, 3, 4}
print("Is set1 a subset of set2?", is_subset(set1, set2))
