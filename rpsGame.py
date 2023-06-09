# Rock Paper Scissor
import random


class Player:
    def __init__(self):
        self.gestures = ["rock", "paper", "scissors"]
        self.result = ""
        self.score = 0

    def choose_gesture(self):
        raise NotImplementedError(
            "Abstract method 'choose_gesture' must be implemented.")
        # pass

    def increment_score(self):
        self.score += 1


class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input("Enter your name: ")

    def choose_gesture(self):
        self.result = input(
            "Choose a gesture[rock(R),paper(P),scissors(S)]: ").lower()
        if self.result == "r":
            self.result = "rock"
        elif self.result == "p":
            self.result = "paper"
        elif self.result == "s":
            self.result = "scissors"


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Computer"

    def choose_gesture(self):
        self.result = random.choice(self.gestures)


class Game:
    def __init__(self, player1: object, player2: object, rounds=1):
        self.player1 = player1
        self.player2 = player2
        self.score = 0
        self.rounds = rounds

        # Rules tell you which gesture beats which gesture
        self.rules = {
            "rock": ["scissors"],   # rock win scissors
            "paper": ["rock"],      # paper win rock
            "scissors": ["paper"],  # scissor win paper
        }

        print("Welcome to Rock, Paper, Scissors Game!!!")

        # set round to play
        self.rounds = int(input("How many rounds to play: "))
        print(f"{self.player1.name} vs {self.player2.name}")

    def compare_gestures(self):
        result1 = self.player1.result
        result2 = self.player2.result

        # Same gesture
        if result1 == result2:
            print("It's a tie!")
        elif result1 in self.rules[result2]:
            print(f"{self.player2.name} wins!")
            self.player2.increment_score()
        else:
            print(f"{self.player1.name} wins!")
            self.player1.increment_score()

    def start(self):
        for i in range(self.rounds):
            print(f"Round{i+1}")
            self.player1.choose_gesture()
            self.player2.choose_gesture()

            if self.player1.result == "exit" or self.player2.result == "exit":
                break

            print(f"{self.player1.name} choose: {self.player1.result}")
            print(f"{self.player2.name} choose: {self.player2.result}")

            self.compare_gestures()
            print(
                f"Score: {self.player1.name} vs {self.player2.name} : {self.player1.score} - {self.player2.score}")


human = Human()
computer = Computer()
computer1 = Computer()
computer2 = Computer()

game = Game(human, computer)
game.start()


# # Rules tell you which gesture beats which gesture
#         self.rules = {
#             # "rock": ["scissors", "s"],
#             # "paper": ["rock", "r"],
#             # "scissors": ["paper", "p"],
#             # "r": ["scissors", "s"],
#             # "p": ["rock", "r"],
#             # "s": ["paper", "p"]
#             "r": ["s"],  # rock win scissors
#             "p": ["r"],  # paper win rock
#             "s": ["p"]  # scissor win paper
#         }
