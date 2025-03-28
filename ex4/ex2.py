# Author: Damian Zukowski

class NumberStats:
    def __init__(self):
        #no need to add any new variables here, just change the
        #initialization of the self.numbers variable.
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        if self.numbers:    # check if any numbers are added
            nums_sum = sum(self.numbers)
            return nums_sum
        else:
            return 0
        
    def average(self):
        if self.numbers:    # check if any numbers are added
            mean = self.get_sum() / self.count_numbers()
            return mean
        else:
            return 0


if __name__ == "__main__":
    stats = NumberStats()

    #Part 1 test prints:
    """stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())"""
    #Part 2 test prints:
    """stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())"""

    # Part 3
    def userInputs(stats):
        while True:
            try:
                num = int(input("Part 3: Please enter an integer (-1 to stop): "))
                if num == -1:
                    break
                stats.add_number(num)

            except ValueError:
                print("Wrong input!")

    # Calling the function for inputs and printing the results after its done
    userInputs(stats)
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())

    # Part 4

    # Modified original function from part 3
    def userInputs2(all_nums, even_nums, odd_nums):
        while True:
            try:
                num = int(input("Part 4: Please enter an integer (-1 to stop): "))
                if num == -1:
                    break
                all_nums.add_number(num)    # Will always add every number, except -1

                # Check if the number is even or not -> add to the correct object
                if num % 2 == 0:
                    even_nums.add_number(num)
                else:
                    odd_nums.add_number(num)

            except ValueError:
                print("Wrong input!")

    # Initializing 3 objects
    all_nums = NumberStats()
    even_nums = NumberStats()
    odd_nums = NumberStats()

    userInputs2(all_nums, even_nums, odd_nums)

    # print checks
    print("Sum of all numbers:", all_nums.get_sum())
    print("Sum of even numbers:", even_nums.get_sum())
    print("Sum of odd numbers:", odd_nums.get_sum())
    print("Mean of all numbers:", all_nums.average())

