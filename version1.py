import random
from typing import List, Tuple, Callable
import csv

# I will try my best to document the code here so that it is easily accessible to everyone.

class PrisonersDilemma:
    def __init__(self):
        # Below is the matrix of rewards for cooperating and defecting.
        self.payoff_matrix = {
            ('cooperate', 'cooperate'): (3, 3),
            ('cooperate', 'defect'): (0, 5),
            ('defect', 'cooperate'): (5, 0),
            ('defect', 'defect'): (1, 1)
        }

    def play_round(self, move1, move2) -> Tuple[int, int]:
        # The function runs one round between two players, returning the points for the round.
        return self.payoff_matrix[(move1, move2)]

class Bot:
    def __init__(self, name: str, strategy: Callable[[List[Tuple[str, str]]], str]):
        self.name = name
        self.score = 0
        self.strategy = strategy

    def make_move(self, history: List[Tuple[str, str]]) -> str:
        return self.strategy(history)

def run_simulation(game: PrisonersDilemma, bot1: Bot, bot2: Bot, rounds: int) -> Tuple[int, int]:
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

def always_defect(history: List[Tuple[str, str]]) -> str:
    return 'defect'

def always_cooperate(history: List[Tuple[str, str]]) -> str:
    return 'cooperate'

def tit_for_tat(history: List[Tuple[str, str]]) -> str:
    if not history:
        return 'cooperate'
    return history[-1][1]  # Copy opponent's last move

def random_choice(history: List[Tuple[str, str]]) -> str:
    return random.choice(['cooperate', 'defect'])

def joe(history):
    chance = random.random()
    if history:
        if history[-1][1] == 'defect':
            return 'defect'
    if chance < 0.5:
        return 'defect'
    else:
        return 'cooperate'
    
def danny(history):
    if not history:
        return 'cooperate'  
    if history[-1][1] == 'defect':
        return 'defect'
    return 'cooperate'

def Hyeon(history):
    if not history:
        return 'cooperate'
    else:
        return 'defect'

def gustavo(history):
    if not history:
        return "defect"
    if history[-1][1] == "defect":
            return "defect"
    else:
        chance = random.randint(0,100)
        if chance < 95:
            return 'defect'
        else:
            return 'cooperate'
        
def copykitr(history: List[Tuple[str, str]]) -> str:
    if not history:
        return 'cooperate'
    if history[-1][1] == 'cooperate':
        return history[-1][1]
    if history[-1][1] == 'defect':
        if len(history)>2:
            if history [-2][1] == 'defect':
                return 'defect'
            else:
                return 'cooperate'
        else:
            return 'cooperate'

def madness(history: List[Tuple[str, str]]) -> str:
    if not history:
        return 'defect'
    if history[-1][1] == 'defect':
        return 'cooperate'
    if history[-1][1] == 'cooperate':
        return 'defect'

def checkLastThree(history):
    howMuchDefect = 0
    if len(history) > 2:
        scope = history[-2:]
        for i in scope:
            if i[1] == 'defect':
                howMuchDefect += 1
        if howMuchDefect > 2:
            return 'defect'
    return 'cooperate'

def giyushino(history: List[Tuple[str, str]]) -> str:
    if not history:
        return 'cooperate'
    if len(history) > 3:
        last_4_opponent_moves = [move[1] for move in history[-4:]]
        if last_4_opponent_moves == ['defect', 'defect', 'defect', 'defect']:
            return "defect"
        elif last_4_opponent_moves == ['cooperate', 'cooperate', 'cooperate', 'cooperate']:
            return "defect"
        else:
            if history[-1][1] == "cooperate":
                return "cooperate"
            else:
                x = random.choice(last_4_opponent_moves)
                return x
    else:
        if history[-1][1] == 'cooperate':
            return "cooperate"
        else:
            return "defect"

def Bains(history):
    chance = random.randint(1,10)
    if history:
        if history[-1][1] =='cooperate':
            return 'cooperate'
        if chance <= 3:
            return 'cooperate'
        else:
            return 'defect'
    return 'cooperate'

def dannyDefect(history):
    return 'defect'

def gustavoSecond(history):
    if not history:
        return "defect"
    if history[-1][1] == "defect":
            return "defect"
    if history[-1][1] == "cooperate":
        return "defect"
    if len(history) >80:
        return "defect"
    else:
        chance = random.randint(0,100)
        if chance < 95:
            return 'defect'
        else:
            return 'cooperate'


def simon_last_turn_defect(history: List[Tuple[str, str]]) -> str:
    #Cooperate on the first turn
    if not history:
        return 'cooperate'
    #Defect on the last turn
    elif len(history) < 3:
      return random.choice(['cooperate', 'defect'])
      #Otherwise copy the opponent's last move
    else:
      return history[-1][1]

def Sujith(history: List[Tuple[str, str]]) -> str:
    if len(history) < 2:
        return 'cooperate'
    if history[-1][1] == history[-2][1]:
        return history[-1][1]
    else:
        return 'defect'

def Rock_2(history: List[Tuple[str, str]]) -> str:
    if not history:
        return 'cooperate'
    
    if history[-1][1] == history[-1][0]:
        return 'defect'
    return 'cooperate'  # or 'defect'

def gamblingbutbetter(history: List[Tuple[str, str]]) -> str:
    i = random.randint(0,644)
    if i == 0:
        return "cooperate"
    
    return "defect"

def exploitnoobs(history):
    if not history:
        return "cooperate"
    if len(history) < 2:
        return "cooperate"
    return 'defect'

def Rock_1(history: List[Tuple[str, str]]) -> str:
    if not history:
        return 'cooperate'
    if history[-1][1] == 'cooperate':
        return 'defect'
    return 'cooperate'

#Second Instance: Always Defect
def simon_1(history: List[Tuple[str, str]]) -> str:
    return 'defect'

def garymccready(history: List[Tuple[str, str]]) -> str:
    max = 500 - len(history)
    garymccreadychance = random.randint(1,max)

    if garymccreadychance > 374: 
        return 'cooperate'
    else:
        return 'defect'

def copykitr2(history: List[Tuple[str, str]]) -> str:
    copykitr2chance = random.randint(1, 10)
    if not history:
        if copykitr2chance == 1:
            return 'defect'
        else:
            return 'cooperate'
    if history[-1][1] == 'cooperate':
        if copykitr2chance == 1:
            return 'defect'
        else:
            return 'cooperate'
    if history[-1][1] == 'defect':
        if len(history)>2:
            if history [-2][1] == 'defect':
                if copykitr2chance == 1:
                    return 'cooperate'
                else:
                    return 'defect'
            elif copykitr2chance == 1:
                return 'defect'
            else:
                return 'cooperate'
        elif copykitr2chance == 1:
            return 'defect'
        else:
            return 'cooperate'
 

def glass(history: List[Tuple[str, str]]) -> str:
    glasschance = random.randint(1,4)
    if glasschance == 1:
        return 'defect'
    else:
        return "cooperate"

def last_straw(history: List[Tuple[str, str]]) -> str:
    max = 10
    last_strawchance = random.randint(1,max)
    if last_strawchance == 1:
        max = 1
        return "defect"
    else:
        return "cooperate"
 

def Rock_3(history: List[Tuple[str, str]]) -> str:
    if not history:
        return 'cooperate'
    if len(history) > 2:
        if history[-1][0] == history[-1][1] and history[-2][0] == history[-2][1]:
            return 'cooperate'
        if history[-1][1] == 'defect':
            return 'defect'
    return 'cooperate'  # or 'defect'


def glass(history: List[Tuple[str, str]]) -> str:
    glasschance = random.randint(1,4)
    if glasschance == 1:
        return 'defect'
    else:
        return 'cooperate'

def last_straw(history: List[Tuple[str, str]]) -> str:
    max = 500
    last_strawchance = random.randint(1,max)
    if last_strawchance == 1:
        return 'defect'
    if len(history)>1:
        if history[-1][0] == 'defect':
            return 'defect'
        else: 
            return 'cooperate'
    else:
        return 'cooperate'
    
def kitcat_tm(history: List[Tuple[str, str]]) -> str:
    kitcat_tmchance = random.randint(1, 10)
    if not history:
        if kitcat_tmchance == 1:
            return 'defect'
        else:
            return 'cooperate'
    if history[-1][1] == 'cooperate':
        if kitcat_tmchance == 1:
            return 'defect'
        else:
            return 'cooperate'
    if history[-1][1] == 'defect':
        if kitcat_tmchance == 1:
            return 'cooperate'
        else:
            return 'defect'
        
def gustavo_3(history):
    if not history:
        return "cooperate"
    if history[-1][1] == "cooperate":
        return "cooperate"
    else:
        chance = random.randint(0,100)
        if chance < 95:
            return 'defect'
        else:
            return 'cooperate'
def doggo(history: List[Tuple[str, str]]) -> str:
    if len(history)>1:
        if history [-1][0] == 'defect':
            return 'defect'
        else:
            return 'cooperate'
    if len(history)>2:
        if history[-2][1] == 'defect':
            if history[-1][1] == 'defect':
                return 'defect'
            else:
                return 'cooperate'
        else:
            return 'cooperate'
    else:
        return 'cooperate'

def gustavo_6(history):
    if not history:
        return "defect"
    if history[-1][1] == "defect":
        return "defect"
    else:
        return "cooperate"
        
def joeTry1(history):
    if not history:
        return "cooperate"
    if len(history) > 1:
        if history[-2][0] == "defect" and history[-1][1] == "cooperate":
            return "defect"
    if history[-1][1] == "cooperate":
        return "cooperate"
    else:
        chance = random.random()
        if chance < 0.97:
            return 'defect'
    return "cooperate"

def joeEvil(history):
    if not history:
        return "cooperate"
    if len(history) == 3:
        return "defect"
    if len(history) > 1:
        if history[-2][0] == "defect" and history[-1][1] == "cooperate":
            return "defect"
    if history[-1][1] == "cooperate":
        return "cooperate"
    else:
        chance = random.random()
        if chance < 0.97:
            return 'defect'
    return "cooperate"

def dannyCopy(history):
    if not history:
        return 'cooperate' 
    return history[-1][1]

def simpl(history: List[Tuple[str, str]]) -> str:
    if len(history) >= 3:
        if history[-3][1] == "cooperate" and history[-2][1] == "cooperate" and history[-1][1] == "cooperate":
            return "cooperate"
    return "defect"

def peanut(history: List[Tuple[str, str]]) -> str:
    if not history:
        return 'defect'
    if history[-1][1] == 'cooperate':
        return 'defect'
    if history [-1][1] == 'defect':
        return 'cooperate'

def insanity(history: List[Tuple[str, str]]) -> str:
    if len(history) == 0:
        return 'cooperate'
    if len(history) == 1:
        return 'defect'
    else:
        return history[-2][1]

def cruelty(history: List[Tuple[str, str]]) -> str:
    if len(history)<3:
        return 'cooperate'
    else:
        return history[-2][1]
        
def Bains2(history):
   if not history:
       return 'cooperate'
   else:
       if len(history) %2== 0 and history [-1][1] == 'cooperate':
           return 'cooperate'
       else:
           return 'defect'

def Sujith2(history: List[Tuple[str, str]]) -> str:
    if len(history) >= 3:
        if history[-1][1] == history[-2][1] == history[-3][1]:
            if history[-1][1] == 'cooperate':
                return 'defect'
            elif history[-1][1] == 'defect':
                return 'defect'
            else:
                return 'cooperate'
        else:
            return "defect"
    return 'cooperate'
 
def gustavo_5(history):
    if not history:
        return "cooperate"
    if history[-1][1] == "cooperate":
        chance = random.randint(0,100)
        if chance < 95:
            return 'defect'
        else:
            return 'cooperate'
    else:
        chance = random.randint(0,100)
        if chance < 85:
            return 'defect'
        else:
            return 'cooperate'

def Rock_4(history: List[Tuple[str, str]]) -> str:
    if not history:
        return 'cooperate'
    if len(history) > 2:
        if history[-1][0] ==  history[-2][0] == 'cooperate':
            return 'defect'
        if history[-1][1] ==  history[-1][-1] == 'cooperate':
            return 'defect'
    return 'cooperate'  # or 'defect'

def Sujith3(history: List[Tuple[str, str]]) -> str:
    chance = random.randint(1, 100)
    if not history:
        return 'cooperate'
    else:
        if chance <= 90:
            return 'defect'
        else:
            return 'cooperate'

def gustavo_4(history):
    chance = random.randint(0,100)
    if len(history) > 80:
        return "defect"
    if chance > 50:
        return "defect"
    else:
        return "cooperate"
    
def Sujith3(history: List[Tuple[str, str]]) -> str:
    chance = random.randint(1, 100)
    if not history:
        return 'cooperate'
    else:
        if chance <= 90:
            return 'defect'
        else:
            return 'cooperate'

def main():
    game = PrisonersDilemma()
    # IMPORTANT: ADD YOUR BOT HERE WITH THE NAME TO YOUR FUNCTION.
    bots = [
        Bot("Peanut",peanut),
        Bot("Rocks fat bot", Rock_4),
        Bot("Sujith3", Sujith3),
        Bot("Gustavo6", gustavo_6),
        Bot("Gavin's Simpl",simpl),
        Bot("joe is better", joeTry1),
        Bot("Last Straw", last_straw),
        Bot("Rock_3", Rock_3),
        Bot("glass", glass),
        Bot("copykitr2", copykitr2),
        Bot("Always Defect", always_defect),
        Bot("Tit for Tat", tit_for_tat),
        Bot("Random", random_choice),
        Bot("Danny's copy", dannyCopy),
        Bot("Dog", doggo),
        Bot("Joe's Bot", joeEvil),
        Bot("Danny's first", danny),
        Bot("Hyeon's First", Hyeon),
        Bot("Gustavo's First", gustavo),
        Bot("Sahib's", Bains),
        Bot("Checks 3", checkLastThree),
        Bot("copykitr", copykitr),
        Bot("madness", madness),
        Bot("Danny's Defect", dannyDefect),
        Bot("giyushino",giyushino),
        Bot("gustavoSecond",gustavoSecond),
        Bot("Simon",simon_last_turn_defect),
        Bot("Gambling", gamblingbutbetter),
        Bot("Rock's First", Rock_1),
        Bot("Greedy Gary", garymccready),
        Bot("Simon's Defect", simon_1),
        Bot("Rock 2", Rock_2),
        Bot("Sujith",Sujith),
        Bot("Gustavo5", gustavo_5),
        Bot("Joe's Try",exploitnoobs),
        Bot("Kitcat", kitcat_tm),
        Bot("Gustavo3", gustavo_3),
        Bot("Sujith",Sujith2),
        Bot("Gustavo4", gustavo_4),
        Bot("Bains2", Bains2),
        Bot("Insanity", insanity),
        Bot("Cruelty", cruelty)
    ]

    rounds = random.randint(90,110)
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

    with open('round_robin_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile) # Write header
        writer.writerow([''] + [bot.name for bot in bots]) # Write data
        writer.writerows(matrix)

    print(f"Results after {rounds} rounds have been saved to 'round_robin_results.csv'")
        
    with open('final_scores.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Bot", "Points"])  # Add header
        sorted_bots = sorted(bots, key=lambda x: x.score, reverse=True)
        for bot in sorted_bots:
            writer.writerow([bot.name, bot.score])
if __name__ == "__main__":
    main()