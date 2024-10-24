import random
from typing import List, Tuple, Callable
import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

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
        self.total_score = 0
        self.strategy = strategy

    def make_move(self, history: List[Tuple[str, str]]) -> str:
        '''Standardizes the code to call the strategy'''
        return self.strategy(history)

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

# ----- Add your bot here! You can look at the previous code for some inspiration.

def adaptive_strategy(history: List[Tuple[str, str]]) -> str:
    if not history:
        return 'cooperate'  # Start by cooperating

    opponent_moves = [move[1] for move in history]
    my_moves = [move[0] for move in history]
    total_rounds = len(history)

    # Calculate opponent's defection rate
    defection_rate = opponent_moves.count('defect') / total_rounds

    # If the opponent always cooperates
    if defection_rate == 0:
        # Defect occasionally to exploit
        if total_rounds % 10 == 0:
            return 'defect'
        else:
            return 'cooperate'
    # If the opponent always defects
    elif defection_rate == 1:
        return 'defect'
    # If the opponent mirrors your moves (Tit for Tat)
    elif total_rounds >= 2 and opponent_moves[-1] == my_moves[-2]:
        return 'cooperate'
    # If the opponent defected last turn
    elif opponent_moves[-1] == 'defect':
        # Defect in retaliation
        return 'defect'
    else:
        # Default to cooperation
        return 'cooperate'

def tit_for_tat_nice(history: List[Tuple[str, str]]):
    # Cooperate first
    if not history:
        return 'cooperate'
    
    # Do tit for tat, but sometimes cooperate if you defected last round
    # This has a chance of beating tit for tat and adaptive in some matchups
    # Based off Axelrod's Tournament and successful strategies: https://en.wikipedia.org/wiki/Prisoner%27s_dilemma 
    last_move = history[-1][1] 
    if last_move == 'defect' and random.random() < 0.05:
        return 'cooperate'
    return  last_move 


def run_simulation(game: PrisonersDilemma, bot1: Bot, bot2: Bot, rounds: int) -> Tuple[int, int, List[dict]]:
    '''Running the simulation and recording detailed match history.'''
    history = []
    gamescore1 = 0
    gamescore2 = 0
    match_history = []
    for round_number in range(1, rounds + 1):
        move1 = bot1.make_move(history)
        # Reverse history for bot2. The first element in the array is always the bot's own move.
        move2 = bot2.make_move([(m2, m1) for m1, m2 in history])
        score1, score2 = game.play_round(move1, move2)
        gamescore1 += score1
        gamescore2 += score2
        history.append((move1, move2))

        # Record the detailed history
        match_history.append({
            'Round': round_number,
            'Bot1_Name': bot1.name,
            'Bot2_Name': bot2.name,
            'Bot1_Move': move1,
            'Bot2_Move': move2,
            'Bot1_Score': score1,
            'Bot2_Score': score2,
            'Bot1_Cumulative_Score': gamescore1,
            'Bot2_Cumulative_Score': gamescore2
        })

    bot1.total_score += gamescore1
    bot2.total_score += gamescore2
    return gamescore1, gamescore2, match_history

def main():
    game = PrisonersDilemma()
    # IMPORTANT: ADD YOUR BOT HERE WITH THE NAME TO YOUR FUNCTION.
    bots = [
        Bot("Always Defect", always_defect),
        Bot("Always Cooperate", always_cooperate),
        Bot("Tit for Tat", tit_for_tat),
        Bot("Random", random_choice),
        Bot("Adaptive Bot", adaptive_strategy),  # Added your adaptive bot here
        Bot("Tit for Tat Nice", tit_for_tat_nice) # Little nicer tit for tat
    ]

    rounds = 100
    results = {}
    all_match_histories = []

    # Create output directories if they don't exist
    os.makedirs('results', exist_ok=True)
    os.makedirs('plots', exist_ok=True)

    # Run simulations
    for i in range(len(bots)):
        for j in range(i + 1, len(bots)):  # This ensures each pair plays only once
            bot1, bot2 = bots[i], bots[j]
            score1, score2, match_history = run_simulation(game, bot1, bot2, rounds)
            results[(bot1.name, bot2.name)] = f"{score1} - {score2}"
            results[(bot2.name, bot1.name)] = f"{score2} - {score1}"  # Add reverse matchup, just makes matrix look nicer.

            # Save detailed match history
            df_match = pd.DataFrame(match_history)
            filename = f'results/{bot1.name}_vs_{bot2.name}.csv'
            df_match.to_csv(filename, index=False)
            all_match_histories.append(df_match)

            # Generate plots for this match
            plt.figure(figsize=(10, 6))
            plt.plot(df_match['Round'], df_match['Bot1_Cumulative_Score'], label=bot1.name)
            plt.plot(df_match['Round'], df_match['Bot2_Cumulative_Score'], label=bot2.name)
            plt.title(f'Cumulative Scores: {bot1.name} vs {bot2.name}')
            plt.xlabel('Round')
            plt.ylabel('Cumulative Score')
            plt.legend()
            plt.savefig(f'plots/{bot1.name}_vs_{bot2.name}_scores.png')
            plt.close()

    # Create the matrix
    matrix = [[bot.name] + [results.get((bot.name, opponent.name), "") for opponent in bots] for bot in bots]

    # Write the round-robin results to CSV
    with open('round_robin_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow([''] + [bot.name for bot in bots])
        # Write data
        writer.writerows(matrix)

    print(f"Results after {rounds} rounds have been saved to 'round_robin_results.csv'")

    # Write the final scores to CSV
    with open('final_scores.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Bot Name', 'Total Score'])
        for bot in bots:
            writer.writerow([bot.name, bot.total_score])

    # Generate summary statistics
    df_all_matches = pd.concat(all_match_histories, ignore_index=True)
    summary_stats = df_all_matches.groupby(['Bot1_Name']).agg({
        'Bot1_Score': ['mean', 'sum'],
        'Bot2_Score': ['mean', 'sum']
    }).reset_index()
    summary_stats.columns = ['Bot Name', 'Average Score For', 'Total Score For', 'Average Score Against', 'Total Score Against']
    summary_stats.to_csv('summary_statistics.csv', index=False)

    # Overall Performance Plot
    total_scores = {bot.name: bot.total_score for bot in bots}
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(total_scores.keys()), y=list(total_scores.values()))
    plt.title('Total Scores of Bots')
    plt.xlabel('Bot Name')
    plt.ylabel('Total Score')
    plt.savefig('plots/Total_Scores.png')
    plt.close()

    print("Summary statistics and plots have been saved.")

if __name__ == "__main__":
    main()
