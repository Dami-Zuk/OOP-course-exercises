# Author: Damian Zukowski

# Task 7

def squared_terms(i):
    squared = i ** 2
    return squared

def ex7():
    max_value = int(input("Enter a maximum AP value: "))
    counter = -1
    sum_of_terms = 0
    squared_sum = 0

    for i in range(0, max_value+1, 3):
        counter += 1
        sum_of_terms += i
        squared_sum += squared_terms(i)

    print("Number of terms: ", counter)
    print("Sum of terms: ", sum_of_terms)
    print("Sum of squared terms: ", squared_sum)


ex7()
