def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6]
print("Even numbers:", filter_even_numbers(numbers))
