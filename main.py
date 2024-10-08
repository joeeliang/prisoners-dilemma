import random
from typing import List, Tuple

class PrisonersDilemma:
    def __init__(self):
        self.payoff_matrix = {
            ('cooperate', 'cooperate'): (3, 3),
            ('cooperate', 'defect'): (0, 5),
            ('defect', 'cooperate'): (5, 0),
            ('defect', 'defect'): (1, 1)
        }

    def play_round(self, move1: str, move2: str) -> Tuple[int, int]:
        return self.payoff_matrix[(move1, move2)]

class Bot:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def make_move(self, history: List[Tuple[str, str]]) -> str:
        raise NotImplementedError("Subclasses must implement make_move method")

class AlwaysDefectBot(Bot):
    def make_move(self, history: List[Tuple[str, str]]) -> str:
        return 'defect'

class AlwaysCooperateBot(Bot):
    def make_move(self, history: List[Tuple[str, str]]) -> str:
        return 'cooperate'

class TitForTatBot(Bot):
    def make_move(self, history: List[Tuple[str, str]]) -> str:
        if not history:
            return 'cooperate'
        return history[-1][1]  # Copy opponent's last move

class RandomBot(Bot):
    def make_move(self, history: List[Tuple[str, str]]) -> str:
        return random.choice(['cooperate', 'defect'])

def run_simulation(game: PrisonersDilemma, bot1: Bot, bot2: Bot, rounds: int) -> Tuple[int, int]:
    history = []
    for _ in range(rounds):
        move1 = bot1.make_move(history)
        move2 = bot2.make_move([(m2, m1) for m1, m2 in history])  # Reverse history for bot2
        score1, score2 = game.play_round(move1, move2)
        bot1.score += score1
        bot2.score += score2
        history.append((move1, move2))
    return bot1.score, bot2.score

def main():
    game = PrisonersDilemma()
    bots = [
        AlwaysDefectBot("Always Defect"),
        AlwaysCooperateBot("Always Cooperate"),
        TitForTatBot("Tit for Tat"),
        RandomBot("Random")
    ]

    rounds = 100
    results = []

    for i in range(len(bots)):
        for j in range(i + 1, len(bots)):
            bot1, bot2 = bots[i], bots[j]
            score1, score2 = run_simulation(game, bot1, bot2, rounds)
            results.append((bot1.name, bot2.name, score1, score2))

    print(f"Results after {rounds} rounds:")
    for bot1_name, bot2_name, score1, score2 in results:
        print(f"{bot1_name} vs {bot2_name}: {score1} - {score2}")

if __name__ == "__main__":
    main()