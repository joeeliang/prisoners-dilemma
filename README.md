**Prisoners Dilemma Social Experiment**
=====================================

**Introduction**
---------------

This project simulates a Prisoner's Dilemma game between different bots, each with its own strategy. The goal is to observe how different strategies interact with each other and which ones emerge as the most successful.

**How to Participate**
----------------------

1. **Create a new bot**: Define your bot's strategy as a function that takes a list of tuples (representing the game history) and returns either 'cooperate' or 'defect'.
2. Add your new bot to the `bots` list in the `main` function. Give your bot a unique name!
3. **Run the simulation**: Run the `main` function to simulate the game between all bots, including yours.
4. **Review the results**: Check the `round_robin_results.csv` file to see how your bot performed against other bots in a matrix format. The `final_results.csv` shows a sum of all points.

**Example Bot Strategies**
---------------------------

* `always_defect`: Always defects, regardless of the game history.
* `always_cooperate`: Always cooperates, regardless of the game history.
* `tit_for_tat`: Cooperates on the first move, then mirrors the opponent's previous move.
* `random_choice`: Randomly chooses to cooperate or defect.

**Adding a New Bot**
---------------------

To add a new bot, follow these steps:

1. Define a new function that takes a list of tuples (representing the game history) and returns either 'cooperate' or 'defect'. For example:
```python
def my_strategy(history: List[Tuple[str, str]]) -> str:
    # Your strategy logic here
    return 'cooperate'  # or 'defect'
```
2. Add a new bot to the `bots` list in the `main` function:
```python
bots = [
    #... existing bots...
    Bot("My Bot", my_strategy)
]
```
**Running the Simulation**
---------------------------

To run the simulation, simply execute the `main` function. The simulation will run for 100 rounds between all bots, and the results will be saved to `round_robin_results.csv` and `final_scores.csv`.

**Results**
------------

The `round_robin_results.csv` file contains a matrix showing the scores for each matchup between bots. The `final_scores.csv` file contains the total score for each bot.

**Tips and Variations**
-----------------------

* Experiment with different strategies and observe how they interact with each other.
* Try modifying the payoff matrix to change the game dynamics.
* Add more bots to the simulation to see how different strategies perform in a larger population.

**Contributing**
----------------

Feel free to contribute to this project by adding new bot strategies, modifying the game dynamics, or improving the simulation code.
