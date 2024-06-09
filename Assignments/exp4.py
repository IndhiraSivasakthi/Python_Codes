def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

# Example usage:
numbers = [1, 2, 3, 4, 5]
print("Second largest number:", second_largest(numbers))
