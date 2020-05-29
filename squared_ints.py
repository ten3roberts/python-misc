import random

# Given a sorted array of integers, where 1 <= N < 10000 and -10000 < array[i] < 10000
# Returns a sorted array containing the squares of the integers

# The solution is linear in complexity


def squared_ints(array):

    if not isinstance(array, list) or len(array) == 0:
        print("Invalid input")
        return

    result = []

    # If array contains no negatives, simply square and return
    if array[0] >= 0:
        for i in range(1, len(array)):
            result.append(array[i] ** 2)
        return result

    # Find the middle 'm' where array[m-1] < 0 and array[m] >= 0
    m = 0

    # Skip first element
    for i in range(1, len(array)):
        if array[i] >= 0 and array[i-1] < 0:
            m = i
            break

    # left iterates backwards from m-1 and array[left] < 0
    left = m-1
    # right iterates forwards from m and array[right] >= 0
    right = m

    result = []

    for i in range(0, len(array)):
        if left < 0:
            result.append(array[right] ** 2)
            right += 1
        elif right >= len(array):
            result.append(array[left] ** 2)
            left -= 1
        # Negative square is going to be bigger
        # If they are equal, left is squared and appended first, in the next generation array[right] is greater or equal
        elif abs(array[left]) < array[right]:
            result.append(array[left] ** 2)
            left -= 1
        else:
            result.append(array[right] ** 2)
            right += 1

    return result


# Test
# Generate a random array
array = []
for i in range(1, 100):
    array.append(random.randint(-10, -1))

array.sort()

print(array)
print(squared_ints(array))
print("---------------------------")
