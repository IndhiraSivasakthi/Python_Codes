def key_exists(d, key):
    return key in d


d = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
print(f"Key '{key}' exists in dictionary:", key_exists(d, key))
