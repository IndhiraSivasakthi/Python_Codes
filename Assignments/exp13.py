def combine_dicts(d1, d2):
    combined = d1.copy()  
    for key, value in d2.items():
        if key in combined:
            combined[key] += value
        else:
            combined[key] = value
    return combined


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 150, 'b': 50, 'd': 400}
print("Combined dictionary:", combine_dicts(d1, d2))
