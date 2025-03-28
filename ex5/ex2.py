# Author: Damian Zukowski

from collections import Counter

class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        counter = Counter(my_list)
        return counter.most_common(1)[0][0]  # Return the most frequent item

    @classmethod
    def doubles(cls, my_list: list):
        counter = Counter(my_list)
        return sum(1 for count in counter.values() if count >= 2)


numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))