import random

def shuffle_list(numbers):
    random.shuffle(numbers)
    return numbers

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

shuffled_numbers = shuffle_list(numbers)
print("Shuffled list:", shuffled_numbers)
