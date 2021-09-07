# Task
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    # Return a sorted array.
    odds = [(i, source_array.index(i)) for i in source_array if i % 2 != 0]
    sorted_odds = sorted([odd[0] for odd in odds])
    sorted_array = source_array.copy()
    for index, odd in enumerate(odds):
        sorted_array.pop(odd[1])
        sorted_array.insert(odd[1], sorted_odds[index])
    return sorted_array

arr = [9, 8, 7, 6, -3, 4, -3, 2, 1, 0]
arr2 = [5, 8, 6, 3, 4]
print(sort_array(arr))