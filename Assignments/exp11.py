def sort_dict_by_values(d, ascending=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))


d = {'apple': 3, 'banana': 1, 'cherry': 2}
print("Sorted dictionary (ascending):", sort_dict_by_values(d, ascending=True))
print("Sorted dictionary (descending):", sort_dict_by_values(d, ascending=False))
