# Author: Damian Zukowski

class Recording:
    def __init__(self, length:int):
        self.__length = length

    # Getter 
    @property   # turns a method into a getter -> allows to access a method like an attribute, no () needed.
    def length(self):
        return f"Length of the recording: {self.__length}"
    
    # Setter
    @length.setter
    def length(self, new_len):
        try:                         # Test if its an integer
            new_len = int(new_len)   
        except ValueError:
            raise ValueError("Wrong length - it must be a number!")
        
        # Assigns new value
        self.__length = new_len
    

# Test object and prints
the_wall = Recording(43)
print("test 1: ", the_wall.length)
the_wall.length = 44
print("test 2: ", the_wall.length)
