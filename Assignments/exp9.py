def index_in_tuple(t, element):
    try:
        return t.index(element)
    except ValueError:
        return -1  

t = (1, 2, 3, 4, 5)
element = 3
print("Index of element:", index_in_tuple(t, element))
