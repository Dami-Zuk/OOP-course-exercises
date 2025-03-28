# Author: Damian Zukowski
import random

# Task 1
def ex1():
    print("Hello")
    return

# Task 2
def ex2():
    num_list = []
    str_list = []

    for i in range(10):
        num_list.append(int(input("Enter a number: ")))
    for i in range(10):
        str_list.append(str(input("Enter a string: ")))

    print("List of numbers: ", num_list, "\nlist of strings: ", str_list)
    for i in range(10):
        num_list.append(random.randint(1, 100))
    print("Random numbers list: ", num_list)
    return

# Task 3
def ex3():
    nums = [5, 99, 3, 2, 1, 77, 69, 420]
    strs = ["dandadan", "grzegorz brzeczyszczykiewicz", "mario", "hey", "badumtsss", "it´s-a-me"]

    nums.sort()
    strs.sort()
    print("Numbers in ascending order: ", nums, "\nWords in alphabetical order: ", strs)
    return

ex3()