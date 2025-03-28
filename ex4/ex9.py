# Author: Damian Zukowski

class WeatherStation:
    def __init__(self, name):
        self.__name = name
        self.__observations = []

    # Adds an observation
    def add_observation(self, observation:str):
        # Check to allow only valid strings
        if observation.isdigit():
            raise ValueError("Wrong input - must be a string.")
            
        self.__observations.append(observation)

    # Returns the latest observation or an empty string if there are none added
    def latest_observation(self):
        # Check if there are any elements in the list
        if self.__observations:
            return f"The latest observation: { self.__observations[-1] }"
        else:
            return " "
        
    # Returns a total number of observations
    def number_of_observations(self):
        return f"Total number of observations: { len(self.__observations) }"
    
    # String representation of the object
    def __str__(self):
        return f"Station name: { self.__name }, { self.number_of_observations() }"
    

# Test object and prints
station = WeatherStation("Houston")

station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())

print(station.number_of_observations())
print(station)