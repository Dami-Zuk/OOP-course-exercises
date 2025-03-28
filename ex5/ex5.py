# Author: Damian Zukowski

class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year
 
class GameWarehouse:
    def __init__(self):
        self._games = []        # Changed from private to protected so subclasses can access it.
 
    def add_game(self, game: ComputerGame):
        self._games.append(game)
 
    def get_games(self):
        return self._games

class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def get_games(self):
        old_games = []
        for game in self._games:
            if game.year < 1990:
                old_games.append(game)

        #return [game for game in self._games if game.year < 1990] - List comprehension
        return old_games


museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))

for game in museum.get_games():
    print(game.name)