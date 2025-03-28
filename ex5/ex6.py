import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)
    
    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                print("It's a tie!")

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

# p = WordGame(3)
# p.play()


# Part 1: The longest word wins; inherits methods from the parent but modifies round_winner.
class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):       # Player 1 wins
            return 1
        elif len(player1_word) < len(player2_word):     # Player 2 wins
            return 2
        else:
            return 0        # A tie
        
# p1 = LongestWord(3)
# p1.play()


# Part 2: The most vowels wins; inherits from the parent but modifies round_winner.
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = ["a", "e", "i", "o", "u", "y"]
        counter_p1 = 0
        counter_p2 = 0

        #for char in player1_word:
            #if char in vowels:
                #counter_p1 += 1
        #for char in player2_word:
            #if char in vowels:
                #counter_p2 += 1

        # List comprehension; more efficient
        counter_p1 = sum(1 for char in player1_word if char in vowels)
        counter_p2 = sum(1 for char in player2_word if char in vowels)

        if counter_p1 > counter_p2:     # Player 1 wins
            return 1
        elif counter_p1 < counter_p2:   # Player 2 wins
            return 2
        else:
            return 0        # A tie

# p2 = MostVowels(3)
# p2.play()
    

# Part 3:
class FiveWordsGame(WordGame):
    def __init__(self, rounds, ):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        correct_choices = ["rock", "paper", "scissors", "lizard", "spock"]

        # Checks if the input is correct
        if player1_word.lower() not in correct_choices and player2_word.lower() not in correct_choices:
            print("Wrong choice! Enter rock, paper, scissors, lizard or Spock only!")
            return None

        # A draw
        if player1_word.lower() == player2_word.lower():
            return 0
        
        # Player 1 win scenarios
        winning_moves = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
        }
        
        if player2_word.lower() in winning_moves[player1_word.lower()]:
            return 1
        
        # Player 2 wins
        else:
            return 2
            

            # Player 1 win scenarios
            # elif player1_word.lower() == "rock" and player2_word.lower() in ["scissors", "lizard"]:
                # return 1
            # elif player1_word.lower() == "paper" and player2_word.lower() in ["scissors", "lizard"]:
                # return 1
            # elif player1_word.lower() == "scissors" and player2_word.lower() in ["paper", "lizard"]:
                # return 1
            # elif player1_word.lower() == "lizard" and player2_word.lower() in ["spock", "paper"]:
                # return 1
            # elif player1_word.lower() == "spock" and player2_word.lower() in ["scissors", "rock"]:
                # return 1

            # Player 2 win scenarios
            # else:
                # return 2


p3 = FiveWordsGame(3)
p3.play()
