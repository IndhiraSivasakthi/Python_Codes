def print_dict(d):
    print("Using loop:")
    for key, value in d.items():
        print(f"{key}: {value}")

    print("\nUsing comprehension:")
    [print(f"{key}: {value}") for key, value in d.items()]

d = {'a': 1, 'b': 2, 'c': 3}
print_dict(d)
