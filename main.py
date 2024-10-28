import random
from typing import List, Tuple, Callable
import csv

# I will try my best to document the code here so that it is easily accessible to everyone.

class PrisonersDilemma:
    '''This is the class that stores the parameters to the prisoners dilemma.'''
    def __init__(self):
        # Below is the matrix of rewards for cooperating and defecting.
        self.payoff_matrix = {
            ('cooperate', 'cooperate'): (3, 3),
            ('cooperate', 'defect'): (0, 5),
            ('defect', 'cooperate'): (5, 0),
            ('defect', 'defect'): (1, 1)
        }

    def play_round(self, move1: str, move2: str) -> Tuple[int, int]:
        # The function runs one round between two players, returning the points for the round.
        return self.payoff_matrix[(move1, move2)]

class Bot:
    '''The template for the bot. Each bot will have a name, a score, and a strategy. Your job is to code a function that acts as the strategy for the bot.'''
    def __init__(self, name: str, strategy: Callable[[List[Tuple[str, str]]], str]):
        self.name = name
        self.score = 0
        self.strategy = strategy

    def make_move(self, history):
        '''Standardizes the code to call the strategy'''
        return self.strategy(history)

# Start here

def always_defect(history):
    return 'defect'

def always_cooperate(history):
    return 'cooperate'

def tit_for_tat(history):
    if not history:
        return 'cooperate'
    return history[-1][1]  # Copy opponent's last move

def random_choice(history):
    return random.choice(['cooperate', 'defect'])

def joe_bot(history):
    return 'cooperate'

# ----- add your bot here! You can look at the previous code for some inspiration. Don't forget to add your bot to the main function below later!

def run_simulation(game: PrisonersDilemma, bot1: Bot, bot2: Bot, rounds: int) -> Tuple[int, int]:
    '''Running the simulation.'''
    history = []
    gamescore1 = 0
    gamescore2 = 0
    for _ in range(rounds):
        move1 = bot1.make_move(history)
        move2 = bot2.make_move([(m2, m1) for m1, m2 in history])  # Reverse history for bot2. The first element in the array is always the bots own move.
        score1, score2 = game.play_round(move1, move2)
        gamescore1 += score1
        gamescore2 += score2
        history.append((move1, move2))
    bot1.score += gamescore1
    bot2.score += gamescore2
    return gamescore1, gamescore2

def main():
    game = PrisonersDilemma()
    # IMPORTANT: ADD YOUR BOT HERE WITH THE NAME TO YOUR FUNCTION.
    # WHATEVER I WANT
    bots = [
        Bot("Always Defect", always_defect),
        Bot("Always Cooperate", always_cooperate),
        Bot("Tit for Tat", tit_for_tat),
        Bot("Random", random_choice),
        Bot("Joe's Bot", joe_bot)
    ]

    rounds = 100
    results = {}

    # Run simulations
    for i in range(len(bots)):
        for j in range(i + 1, len(bots)):  # This ensures each pair plays only once
            bot1, bot2 = bots[i], bots[j]
            score1, score2 = run_simulation(game, bot1, bot2, rounds)
            results[(bot1.name, bot2.name)] = f"{score1} - {score2}"
            results[(bot2.name, bot1.name)] = f"{score2} - {score1}"  # Add reverse matchup, just makes matrix look nicer.

    # Create the matrix
    matrix = [[bot.name] + [results.get((bot.name, opponent.name), "") for opponent in bots] for bot in bots]

    # Write to CSV
    with open('round_robin_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile) # Write header
        writer.writerow([''] + [bot.name for bot in bots]) # Write data
        writer.writerows(matrix)

    print(f"Results after {rounds} rounds have been saved to 'round_robin_results.csv'")

    with open('final_scores.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for bot in bots:
            writer.writerow([bot.name, bot.score])

if __name__ == "__main__":
    main()