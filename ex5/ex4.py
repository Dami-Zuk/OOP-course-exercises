# Author: Damian Zukowski

class Computer:
    def __init__(self, model: str, speed: int):
        self.model = model
        self.speed = speed

    def __str__(self):
        return f"{self.model}, {self.speed} Mhz"
    

class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        super().__init__(model, speed)      # calls parent constructor
        self.weight = weight

    def __str__(self):
        return f"{self.model}, {self.speed} Mhz, {self.weight} kg"
    

pc = Computer("AMD", 666)
laptop = LaptopComputer("Asus", 420, 3)
print(pc)
print(laptop)
