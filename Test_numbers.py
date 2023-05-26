# Task 9

def two_number_sum(numbers,target):
    used_numbers=[]
    for number in numbers:
        search_number = target - number
        if search_number in used_numbers:
            return[number,search_number]
        used_numbers.append(number)
    return []

#possible
numbers = [3, 5, -4, 8, 11, 1, -1]
target = 10
result = two_number_sum(numbers, target)
#possible
numbers = [1, 2, 4, 2, 1, 45, 51, 24]
target = 3
result = set(two_number_sum(numbers, target))
print(result)

#not possible
numbers = [1, 2, 4, 2, 1, 45, 51, 24]
target = 27
result = two_number_sum(numbers, target)
print(result)



