""" Check the example concerning inheritance which was fully introduced during the lectures.
(b) Invent and add a new intance variable for some new feature so that it will
exist at least in three classes. You can make it happen by using inheritance
or direct definitions. (1 points)
(c) Change all classes so that you apply proper encapsulation everywhere. You
need to add encapsulation for instance variables. (1 points)    Getters and Setters
(d) Write at least three tests for each new change in your classes. (1 points)
(e) Now, write a class for dog which will be the subclass for Wolf. Implement its
barking so that dynamic binding will be applied when a dog does what it does. Also
add some other methods. Encapsulate. (2 points)
(f) Write multiple tests for your Dog-class and its features. (1 points)
(g) Add needed preconditions using assert into classes Animal, Mammal, Wolf, and Dog.
There are multiple examples in the codes of lectures that may help you. (1 points) """

class Animal:

    def __init__(self, number_of_legs: int, fur_length: int):
        assert number_of_legs >= 0, "Enter correct number of legs!"
        assert fur_length >=0, "Enter correct length of fur!"

        self._legs = number_of_legs
        self._fur_length = fur_length

        # Instance variables
        self._weight = 0

    def get_legs(self):
        return self._legs
    
    def get_fur_length(self):
        return self._fur_length
    
    def set_weight(self, weight):
        # The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
        assert weight >= 0, "Please enter a correct weight!"
        self._weight = weight

    def get_weight(self):
        return self._weight

    def make_sound(self):
        return "*it's quiet*"


class Cat(Animal):
    def __init__(self, number_of_legs, fur_length, whiskers):
        super().__init__(number_of_legs, fur_length)
        assert whiskers >=0, "Enter correct length of whiskers!"
        self._whiskers_length = whiskers


class Wolf(Animal):
    def __init__(self, number_of_legs, fur_length):
        super().__init__(number_of_legs, fur_length)


class Dog(Wolf):
    def __init__(self, number_of_legs, fur_length):
        super().__init__(number_of_legs, fur_length)

    def bark(self):
        return "Woof!"
    
    def fetch(self):
        return "Fetching a stick!"
    
    def give_paw(self):
        return "Giving the paw!"


# Tests
def animal_test():
    animal = Animal(2, 20)

    animal.set_weight(25)
    print(f"Legs: {animal.get_legs()}, Fur: {animal.get_fur_length()}, Weight: {animal.get_weight()}, Sound: {animal.make_sound()}")


def dog_test():
    doggo = Dog(4, 14)

    doggo.set_weight(22)
    print(f"Legs: {doggo.get_legs()}, Fur: {doggo.get_fur_length()}, Weight: {doggo.get_weight()}, Bark: {doggo.bark()}, Fetch: {doggo.fetch()}, Give paw: {doggo.give_paw()}")


animal_test()
dog_test()


class Leon(Cat):
    def __init__(self, number_of_legs, fur_length, whiskers):
        super().__init__(number_of_legs, fur_length, whiskers)
        self._fur_color = "white-gray"
        self._purring = "loud"
        self._cuddliness = "very"

    def make_sound(self):
        print("MEOOOW")

    def print_infos(self):
        return {
            "no. of legs": self.get_legs(),
            "fur length": self.get_fur_length,
            "whiskers length": self._whiskers_length,
            "fur color": self._fur_color, 
            "purring": self._purring,
            "cuddliness": self._cuddliness,
            }
    
def leon_test():
    my_cat = Leon(4, 15, 7)
    print(my_cat.print_infos())




