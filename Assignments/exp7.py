def common_elements(t1, t2):
    return tuple(set(t1) & set(t2))


t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
print("Common elements:", common_elements(t1, t2))
