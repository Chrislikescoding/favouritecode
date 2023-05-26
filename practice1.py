# - Write a function that accepts an array of number and an integer representing a target sum.
# - If any two numbers from the accepted numbers sum up to the target sum then the function should return them in array,
# in any order.
# - If no numbers sum to the target sum, the function should return an empty array.
# - The target has to be achieved using different numbers from the array.


def find_target_sum(numbers,target):
    used_numbers=[]
    for number in numbers:
        search_number = target - number

        if search_number in used_numbers:
            return[number,search_number]
        used_numbers.append(number)
    return []

numbers = [3, 5, -4, 8, 11, 1, -1]
target = 10

result = find_target_sum(numbers, target)
print(result)