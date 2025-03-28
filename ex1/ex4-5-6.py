# Author: Damian Zukowski

# Task 4
def is_negative(nums):
    counter = 0
    for i in nums:
        if i < 0:
            counter += 1
    return counter

# Task 5
def is_even(nums):
    counter = 0
    for i in nums:
        if i % 2 == 0:
            counter += 1
    return counter

# Task 6
def is_positive(nums):
    sum_of_ints = 0
    for i in nums:
        if i > 0 and i % 3 == 0:
            sum_of_ints += i
    return sum_of_ints


def ex4():
    nums = []

    while True:
        num = int(input("Enter a number: "))
        if num != 0:
            nums.append(num)
        else:
            print("All values: ", nums)
            print("Number of negative values: ", is_negative(nums))
            print("Number of even values: ", is_even(nums))
            print("Sum of positive ints modulo 3: ", is_positive(nums))
            break
    return

ex4()
