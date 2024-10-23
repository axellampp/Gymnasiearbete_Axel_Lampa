# Återskapa Gymnasiearbete 24/25

 Axel Lampa

## För återskapandet

Detta examensarbete undersöker _[fångarnas dilemma]_, det vanligaste problemet man stöter på inom spelteori som ofta används för att analysera och få rationella lösningar i konflikter. Problemet går ut på att två individer måste fatta beslut utan att känna till den andres val. Beroende på deras val kan de antingen samarbeta eller agera själviskt, vilket kommer påverka deras resultat. Genom att replikera och simulera Fångarnas dilemma i Visual Studio Code med Python, syftar examensarbetet till att ge en djupare förståelse för de strategier och tankesätt som används för att få det bästa resultatet.

Ett särskilt fokus ligger på att replikera och analysera Robert Axelrods iteration av _[fångarnas dilemma]_, även känd som _Axelrod’s Tournament_, som publicerades i hans verk _[The Evolution of Cooperation]_. Axelrods forskning visar hur samarbete kan uppstå bland konflikter, och detta examensarbete syftar till att replikera, undersöka och validera hans slutsatser genom flera simuleringar.

|  | **Fånge B är tyst** | **Fånge B vittnar** |
| ------------- | ------------- |---------------|
| **Fånge A är tyst** | $(R, R)$ | $(S, T)$ |
| **Fånge A vittnar** | $(T, S)$ | $(P, P)$ |

där

- $R$ (Reward) är resultatet om båda är tyst
- $T$ (Temptation) är resultatet för att vittna när den andra är tyst
- $S$ (Sucker) är resultatet för att vara tyst medan den andra vittnar
- $P$ (Punishment) är resultatet om båda vittnar

och låt

- $R = 3$
- $T = 5$
- $S = 0$
- $P = 1$

Då får vi denna ojämlikhet: $T$ > $R$ > $P$ > $S$

Anta att båda fångar får slumpmässigt välja sin strategi.

- Låt $x$ vara sannolikheten att fånge A är tyst. Då kan $(1-x)$ vara sannolikheten att fånge A agerar för sitt eget bästa, alltså vittnar.
- Låt $y$ vara sannolikheten att fånge B är tyst. Då kan $(1-y)$ vara sannolikheten att fånge B agerar för sitt eget bästa, alltså vittnar.

Alla möjliga utfall för A kan beräknas utifrån payoff matrisen. Det går som följande:

- Båda är tyst. Detta kan ske med sannolikheten $xy$. Båda fångarna får $R$ som resultat.
- Fånge A är tyst, fånge B vittnar. Detta kan ske med sannolikheten $x(1-y)$. Fånge A får $S$ som resultat.
- Fånge A vittnar, fånge B är tyst. Detta kan ske med sannolikheten $(1-x)y$. Fånge A får $T$ som resultat.
- Båda vittnar. Detta kan ske med sannolikheten $(1-x)(1-y)$. Fånge A får $P$ som resultat.

Förväntade utfall för A blir då summan av allt vilket blir:

$Utfall_A(x, y) = Rxy + Sx(1-y) + Ty(1-x) + P(1-x)(1-y)$

Förenklat så blir detta följande:

$Utfall_A(x, y) = 3xy + 0x(1-y) + 5y(1-x) + 1(1-x)(1-y)$ \
$Utfall_A(x, y) = 3xy + 5y(1-x) + 1(1-x)(1-y)$

För att fortsätta expanderar vi termerna:

$Utfall_A(x, y) = 3xy + 5y-5xy + 1-y-x+xy$

Vilket till sist blir:

$Utfall_A(x, y) = -xy + 4y + 1 - x$

Samma teori gäller för fånge B:

$Utfall_B(x, y) = Rxy + Tx(1-y) + Sy(1-x) + P(1-x)(1-y)$

Däremot så blir den andra och tredje termens koefficient för resultat omvänt eftersom när fånge A vittnar och fånge B håller tyst så får fånge B $S$ och inte $T$. Förenklingar leder till följande:

$Utfall_B(x, y) = Rxy + Tx(1-y) + Sy(1-x) + P(1-x)(1-y)$ \
$Utfall_B(x, y) = 3xy + 5x(1-y) + 0y(1-x) + 1(1-x)(1-y)$ \
$Utfall_B(x, y) = 3xy + 5x −5xy + 1 − y −x + xy$ \
$Utfall_B(x, y) = -xy + 4x + 1 - y$

Nu kan vi kombinera $Utfall_A(x, y)$ och $Utfall_B(x, y)$ för att få ett enat perspektiv:

$Utfall(x, y) = (-xy+4y+1-x) + (xy+4x+1−y)$ \
$Utfall(x, y) = -2xy + 3x + 3y + 2$

## Återskapande

Se till att NumPy, Matplotlib och SciPy är installerade. Detta kan göras som följande i en terminal:

``` bat

python -m pip install numpy
pip install matplotlib
pip install scipy

```

För att återskapa spelet se till att PyGame är installerat. Kan göras vid en terminal som följande:

```bat

pip install pygame

```

Kod för isaritm av individuella utfall.

``` python

import numpy as np
import matplotlib.pyplot as plt

# resolution
x = np.linspace(0, 1, 500)  # More points for better detail
y = np.linspace(0, 1, 500)  # More points for better detail

# meshgrid for the plot
X, Y = np.meshgrid(x, y)

def payoff_function(X, Y):
    return -X * Y + 4 * Y + 1 - X


Z = payoff_function(X, Y)

plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, Z, levels=np.linspace(Z.min(), Z.max(), 50), cmap='YlOrRd')

# contour lines for equilibrium
contour_lines = plt.contour(X, Y, Z, levels=np.linspace(Z.min(), Z.max(), 16), colors='black', linewidths=0.3)

colorbar = plt.colorbar(contour, label='Payoff')
colorbar.set_ticks(np.arange(int(Z.min()), int(Z.max()) + 1))

# Labels and title
plt.title('Payoff Contour Plot for Prisoner A')
plt.xlabel('Probability of Player A Cooperating (x)')
plt.ylabel('Probability of Player B Cooperating (y)')


plt.show()

```

Kod för isaritm av sammanlagda utfall:

``` python

import numpy as np
import matplotlib.pyplot as plt

# resolution
x = np.linspace(0, 1, 500)  # More points for better detail
y = np.linspace(0, 1, 500)  # More points for better detail

# meshgrid for the plot
X, Y = np.meshgrid(x, y)

def payoff_function(X, Y):
    return -2 * X * Y + 3 * X + 3 * Y + 2


Z = payoff_function(X, Y)

plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, Z, levels=np.linspace(Z.min(), Z.max(), 50), cmap='YlOrRd')

# contour lines for equilibrium
contour_lines = plt.contour(X, Y, Z, levels=np.linspace(Z.min(), Z.max(), 16), colors='black', linewidths=0.3)

colorbar = plt.colorbar(contour, label='Payoff')
colorbar.set_ticks(np.arange(int(Z.min()), int(Z.max()) + 1))

# Labels and title
plt.title('Payoff Contour Plot for Prisoner\'s Dilemma')
plt.xlabel('Probability of Player A Cooperating (x)')
plt.ylabel('Probability of Player B Cooperating (y)')


plt.show()

```

Kod för itererade versionen av dilemmat. 13 strategier

``` python
from multiprocessing.sharedctypes import Value
import random
import matplotlib.pyplot as plt
from scipy.stats import chisquare

### Points system instead of years in prison as it is most logical to want as many points as possible than prison years. Thus the table is reversed.
payoff_matrix = {
    ("Cooperate", "Cooperate"): (3, 3),
    ("Cooperate", "Defect"): (0, 5),
    ("Defect", "Cooperate"): (5, 0),
    ("Defect", "Defect"): (1, 1),
}

# Function for simulating one round.
def simulate_round(A_choice, B_choice):
    return payoff_matrix[(A_choice, B_choice)]
    
### Strategies
# Always Cooperate
def strat_cooperator(opponentMoveHistory=None, selfMoveHistory=None):
    return "Cooperate"

# Always Defect
def strat_defector(opponentMoveHistory=None, selfMoveHistory=None):
    return "Defect"

# Randomize the outcome
def strat_random(opponentMoveHistory=None, selfMoveHistory=None):
    return random.choice(["Cooperate", "Defect"])

# Start with cooperating, then copy the opponent's last move.
def strat_titfortat(opponentMoveHistory=None, selfMoveHistory=None):
    if opponentMoveHistory is None or len(opponentMoveHistory) < 1:
        return "Cooperate"
    
    # Check the last move from the opponent
    if opponentMoveHistory[-1] == "Defect":
        return "Defect"

    return "Cooperate"

def strat_titfortwotats(opponentMoveHistory=None, selfMoveHistory=None):
    if opponentMoveHistory is None or len(opponentMoveHistory) < 2:
        return "Cooperate"
    
    # Check the last two moves of the opponent
    if opponentMoveHistory[-1] == "Defect" and opponentMoveHistory[-2] == "Defect":
        return "Defect"

    return "Cooperate"

def strat_joss(opponentMoveHistory=None, selfMoveHistory=None):
    if len(opponentMoveHistory) < 1:  # First round, no previous moves
        return "Cooperate"

    # Introduce a small chance of doing the opposite of the opponent’s last move
    if random.random() < 0.1:
        return "Defect" if opponentMoveHistory[-1] == "Cooperate" else "Cooperate"
    
    # Otherwise, copy the opponent's last move
    return opponentMoveHistory[-1]

# Cooperate until the opponent has defected, then defect forever.
def strat_friedman(opponentMoveHistory=None, selfMoveHistory=None):
    if strat_friedman.hasDefected:
        return "Defect"

    if opponentMoveHistory.count("Defect") > 0:
        strat_friedman.hasDefected = True
        return "Defect"
    
    return "Cooperate"    

# Initialize Friedman-specific variables
strat_friedman.hasDefected = False

# Small function that will ensure that friedman will work for every match
def reset_friedman():
    strat_friedman.hasDefected = False

def strat_davis(opponentMoveHistory=None, selfMoveHistory=None):
    if len(opponentMoveHistory) < 10:
        return "Cooperate"

    if opponentMoveHistory.count("Defect") > 0:
        return "Defect"
    
    return "Cooperate"

# Tit for tat the first 15 rounds. Calculate a net cooperation score where Cooperation: 1 and Defection: -2. If the net cooperation score (NCS) < 0, defect.
# Also have a chance to alter the memory of the opponent's past moves and a change to delete the memory
def strat_memoryDecay(opponentMoveHistory=None, selfMoveHistory=None):
    if opponentMoveHistory is None:
        opponentMoveHistory = []

    round_num = len(opponentMoveHistory)

    NCS_THRESHOLD = 0  # Defect if NCS is below this value
    MEMORY_ALTER_PROB = 0.1  # 5% chance of altering memory
    MEMORY_DELETE_PROB = 0.05  # 5% chance of deleting memory
    TIT_FOR_TAT_ROUNDS = 15  # First 15 rounds as Tit for Tat

    def calculate_ncs(opponent_moves):
        return sum(1 if move == "Cooperate" else -2 for move in opponent_moves)
    
    for i in range(round_num):
        if random.random() < MEMORY_ALTER_PROB:
            opponentMoveHistory[i] = "Defect" if opponentMoveHistory[i] == "Cooperate" else "Cooperate"

    opponentMoveHistory = [move for move in opponentMoveHistory if random.random() >= MEMORY_DELETE_PROB]
    
    if round_num <= TIT_FOR_TAT_ROUNDS:
        if opponentMoveHistory is None or len(opponentMoveHistory) < 1:
            return "Cooperate"
    
        # Check the last two moves of the opponent
        if opponentMoveHistory[-1] == "Defect":
            return "Defect"

        return "Cooperate"

    # After 15 rounds: calculate NCS and adjust strategy
    if round_num > TIT_FOR_TAT_ROUNDS:
        ncs = calculate_ncs(opponentMoveHistory)
        #print(ncs)
        if ncs < NCS_THRESHOLD:
            return "Defect"
        else:
            return "Cooperate"

# Defect first two moves. After the first two moves, alternate based on a probability that increases with opponent's cooperation
def strat_old_tideman_chieruzzi(opponentMoveHistory=None, selfMoveHistory=None):
    # Keep track of opponent's cooperation
    if opponentMoveHistory is None:
        opponentMoveHistory = []

    num_cooperates = opponentMoveHistory.count("Cooperate")
    num_moves = len(opponentMoveHistory)

    # After the first two moves, alternate based on a probability that increases with opponent's cooperation
    if num_moves <= 1:
        return "Defect"
    
    # Calculate cooperation probability (e.g., 0.7 = 7% chance of cooperating)
    if num_moves > 1:
        coop_probability = num_cooperates / num_moves  # Opponent's cooperation rate
        # Add a base probability to ensure a minimum chance of cooperating
        #print(f" chance to coop: {coop_probability}")
        base_probability = 0.3
        final_probability = base_probability + coop_probability * 0.7

        # Make decision based on calculated probability
        if random.random() < final_probability:
            return "Cooperate"
        else:
            return "Defect"

def strat_tideman_chieruzzi(opponentMoveHistory, selfMoveHistory=None):
    round_num = len(opponentMoveHistory)
    num_rounds = 200

    if round_num <= 1:
        strat_tideman_chieruzzi.retaliation_count = 0
        strat_tideman_chieruzzi.consecutive_opponent_defections = 0
        strat_tideman_chieruzzi.last_fresh_start = -20 # 20 rounds ago
        return "Cooperate"


    # Track the opponent’s defections
    if opponentMoveHistory[-1] == "Defect":
        strat_tideman_chieruzzi.consecutive_opponent_defections += 1
    else:
        strat_tideman_chieruzzi.consecutive_opponent_defections = 0

     # Increase retaliation count based on opponent's defection streaks
    if strat_tideman_chieruzzi.consecutive_opponent_defections == 2:
        strat_tideman_chieruzzi.retaliation_count += 1

    # Retaliate by defecting based on the current retaliation count
    if strat_tideman_chieruzzi.retaliation_count > 0:
        strat_tideman_chieruzzi.retaliation_count -= 1
        return "Defect"

    # Check if a 'fresh start' is necessary
    if (strat_tideman_chieruzzi.consecutive_opponent_defections == 0 and 
        round_num - strat_tideman_chieruzzi.last_fresh_start >= 20 and 
        num_rounds - round_num >= 10):

        # Check for 3.0 standard deviations away from a random distribution of defections
        coop_count = opponentMoveHistory.count("Cooperate")
        defect_count = opponentMoveHistory.count("Defect")
        chi2_stat, p_val = chisquare([coop_count, defect_count])

        # Fresh start criteria based on chi-squared test
        if chi2_stat >= 9:  # Approx. 3.0 standard deviations from random
            strat_tideman_chieruzzi.last_fresh_start = round_num
            return "Cooperate"  # Start fresh with two cooperations


    # Defect on the last two moves
    if round_num >= num_rounds - 2:
        return "Defect"

    # Otherwise, play Tit-for-Tat (mirror the opponent’s last move)
    if opponentMoveHistory[-1] == "Cooperate":
        return "Cooperate"
    else:
        return "Defect"

# Initialize strategy-specific variables
strat_tideman_chieruzzi.retaliation_count = 0
strat_tideman_chieruzzi.consecutive_opponent_defections = 0
strat_tideman_chieruzzi.last_fresh_start = -20  # Track fresh start timing

# Play 50 rounds of tit for tat, defect on the 51st round. Then check if opponent is random or tit for tat. Defect if random, tit for tat if tit for tat, otherwise defect every 5 to 15th round.
def strat_graaskamp(opponentMoveHistory=None, selfMoveHistory=None):
    round_num = len(opponentMoveHistory)

    # Tit-for-Tat for the first 50 rounds
    if round_num <= 50:
        if opponentMoveHistory is None or round_num < 1:
            return "Cooperate"
    
        # Check the last two moves of the opponent
        if opponentMoveHistory[-1] == "Defect":
            return "Defect"

        return "Cooperate"
    # Defect on round 51
    if round_num == 51:
        return "Defect"

    # Tit-for-Tat for 5 more rounds (rounds 52-56)
    if 12 <= round_num <= 56:
        # Check the last two moves of the opponent
        if opponentMoveHistory[-1] == "Defect":
            return "Defect"

        return "Cooperate"

    # After round 56, check if opponent is random using chi-squared test
    if round_num == 57:
        # Perform chi-squared test on the opponent's history
        coop_count = opponentMoveHistory.count("Cooperate")
        defect_count = opponentMoveHistory.count("Defect")
        
        if coop_count + defect_count > 0:
            chi2_stat, p_val = chisquare([coop_count, defect_count])

            # If p-value is high, opponent might be random, defect for rest of the game
            if p_val > 0.1:
                strat_graaskamp.random_opponent_detected = True
        #print(p_val)
        # Check if opponent is playing Tit-for-Tat
        if opponentMoveHistory[-3:] == selfMoveHistory[-4:-1]:

            strat_graaskamp.tit_for_tat_detected = True
        #print(f" random: {strat_graaskamp.random_opponent_detected}")
        #print(f" Tit4tat: {strat_graaskamp.tit_for_tat_detected}")
    
    # If random opponent detected, defect forever
    if strat_graaskamp.random_opponent_detected:
        return "Defect"

    # If Tit-for-Tat detected, play Tit-for-Tat
    if strat_graaskamp.tit_for_tat_detected:
        if opponentMoveHistory[-1] == "Defect":
            return "Defect"

        return "Cooperate"

    # Otherwise cooperate and randomly defect every 5 to 15 moves
    if round_num > 57 and strat_graaskamp.defect_counter == 0:
        strat_graaskamp.defect_counter = random.randint(5, 15)

    strat_graaskamp.defect_counter -= 1

    if strat_graaskamp.defect_counter == 0:
        return "Defect"

    return "Cooperate"

# Initialize Graaskamp-specific variables
strat_graaskamp.random_opponent_detected = False
strat_graaskamp.tit_for_tat_detected = False
strat_graaskamp.defect_counter = 0

# Play tit for tat but calculate the opponent's cooperation probability, which decreases over time.
def strat_feld(opponentMoveHistory=None, selfMoveHistory=None):
    round_num = len(opponentMoveHistory)


    # Tit for tat implementation    
    if opponentMoveHistory is None or len(opponentMoveHistory) < 1:
        return "Cooperate"
    
    # Check the last move from the opponent
    if opponentMoveHistory[-1] == "Defect":
        return "Defect"

    # Calculation of cooperation probability
    prob_cooperate = max(1 - (round_num / 400), 0.5)

    # Randomly choose to cooperate based on the calculated probability
    if random.random() < prob_cooperate:
        return "Cooperate"
    else:
        return "Defect"

# Cooperate for 11 rounds, then calculate the opponent's cooperation rate over the last 10 rounds. 
# Then, calculate the cooperation rate as 10% less than the opponent's cooperation rate
def strat_tullock(opponentMoveHistory=None, selfMoveHistory=None):
    round_num = len(opponentMoveHistory)

    if round_num <= 11:
        return "Cooperate"  # Cooperate for the first 11 rounds

    # Calculation of the opponent's cooperation rate
    if round_num > 11:
        last_10_moves = opponentMoveHistory[-10:]
        coop_count = last_10_moves.count("Cooperate")

        # Final calculation of cooperation rate
        prob_cooperate = max(0, (coop_count / 10) - 0.1)

        # Randomly choose to cooperate based on the calculated probability
        if random.random() < prob_cooperate:
            return "Cooperate"
        else:
            return "Defect"

# Let the user be a player and choose to defect or cooperate.       
def strat_human(opponentMoveHistory=None, selfMoveHistory=None):
    while True:
        choice = input("Defect or Cooperate: ").lower()

        if choice.find("d") != -1:
            print("You chose to Defect")
            return "Defect"

        elif choice.find("c") != -1:
            print("You chose to Cooperate")
            return "Cooperate"
        else:
            print(f"'{choice}' is invalid, try again.")

# Define strategies
strategies = [
    strat_cooperator,
    strat_defector,
    strat_random,
    strat_titfortat,
    strat_titfortwotats,
    strat_joss,
    strat_friedman,
    strat_memoryDecay,
    strat_tideman_chieruzzi,
    strat_graaskamp,
    strat_feld,
    strat_tullock,
    strat_davis
]

strategy_names = [
    "Cooperator",
    "Defector",
    "Random",
    "Tit for Tat",
    "Tit for Two Tats",
    "Joss",
    "Friedman",
    "Memory Decay",
    "Tideman and Chieruzzi",
    "Graaskamp",
    "Feld",
    "Tullock",
    "Davis"
]

# simulate_match() simulates a match between 2 strategies
def simulate_match(A_strategy, B_strategy, num_rounds):
    reset_friedman()

    A_score = 0
    B_score = 0

    A_move_history = []
    B_move_history = []

    for _ in range(num_rounds):
        A_choice = A_strategy(B_move_history, A_move_history)
        B_choice = B_strategy(A_move_history, B_move_history)

        # Ensure that choices are valid strings and not lists or other structures
        if isinstance(A_choice, list):  # If a list sneaks in, take the first element
            A_choice = A_choice[0] if A_choice else "Cooperate"
        if isinstance(B_choice, list):
            B_choice = B_choice[0] if B_choice else "Cooperate"

        #print(f"A choice: {A_choice}")
        #print(f"B choice: {B_choice}")

        outcome = simulate_round(A_choice, B_choice)

        A_score += outcome[0]
        B_score += outcome[1]

        A_move_history.append(A_choice)
        B_move_history.append(B_choice)
    
    score = [A_score, B_score]
    #print(f"Player A\'s score: {A_score}")
    #print(f"Player B\'s score: {B_score}")

    return score

# simulate_tournament() simulates the whole tournament for n rounds
def simulate_tournament(num_rounds):

    results = {name: 0 for name in strategy_names}
    for n in range(4):
        for i, strategy_A in enumerate(strategies):
            for j, strategy_B in enumerate(strategies):
                #print(f"Simulating match between {strategy_names[i]} and {strategy_names[j]}")
                A_score, B_score = simulate_match(strategy_A, strategy_B, num_rounds)

                #print(f"Result: {strategy_names[i]} scored {A_score}, {strategy_names[j]} scored {B_score}")
                results[strategy_names[i]] += A_score
                results[strategy_names[j]] += B_score

    return results

def plot_results(results):
    strategies = list(results.keys())
    scores = list(results.values())

    plt.figure(figsize=(10, 6))
    plt.barh(strategies, scores, color=['#AB0003'])
    plt.xlabel('Total Score')
    plt.title(f'Tournament Results of {len(strategies)} strategies')
    plt.grid(axis='x')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    
    num_rounds = 200  # Number of rounds for each match
    tournament_results = simulate_tournament(num_rounds)
    print(tournament_results)

    winner = max(tournament_results, key=lambda name: tournament_results[name])
    winner_score = tournament_results[winner]

    print(f"The winner is '{winner}' who won with a score of {winner_score} points.")

    plot_results(tournament_results)

# Debug
#simulate_match(strat_human, strat_feld, 5) 

```

Kod för det förenklade spelet

``` python
import pygame
import sys
import random

# Color and window configurations
GREEN = (25, 105, 25)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1200
GRAY = (227, 227, 227)
BLACK = (20, 20, 20)

BUTTON_WIDTH = 180
BUTTON_HEIGHT = BUTTON_WIDTH / 2.5
BUTTON_RADIUS = 8

COOPERATE_COLOR = (0, 140, 255)
DEFECT_COLOR = (255, 140, 0)

# Payoff matrix for Prisoner's Dilemma
payoff_matrix = {
    ("Cooperate", "Cooperate"): (3, 3),
    ("Cooperate", "Defect"): (0, 5),
    ("Defect", "Cooperate"): (5, 0),
    ("Defect", "Defect"): (1, 1),
}

# Main game function
def main():
    global SCREEN
    pygame.init()
    pygame.font.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    #SCREEN.fill(GRAY)

    player_total_score = 0
    opponent_total_score = 0
    rounds = 0
    max_rounds = 5
    round_complete = False  # Flag to detect if a round is completed

    player_choice = None
    opponent_choice = None

    while True:
        mouseX, mouseY = pygame.mouse.get_pos()
        SCREEN.fill(GRAY)  # Clear the screen with the background color

        
        cooperate_rect, defect_rect = drawButtons()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not round_complete:
                if cooperate_rect.collidepoint(mouseX, mouseY):
                    player_choice = "Cooperate"
                    opponent_choice = random.choice(["Cooperate", "Defect"])
                elif defect_rect.collidepoint(mouseX, mouseY):
                    player_choice = "Defect"
                    opponent_choice = random.choice(["Cooperate", "Defect"])

        # Once a choice is made, simulate the round and display results
        if player_choice and opponent_choice and not round_complete:
            player_score, opponent_score = simulate_round(player_choice, opponent_choice)
            player_total_score += player_score
            opponent_total_score += opponent_score
            rounds += 1

            # Display result and score
            display_result(player_choice, opponent_choice, player_score, opponent_score)
            display_scores(player_total_score, opponent_total_score, rounds)

            pygame.display.update()  # Update the display to show the result

            # Wait 5 seconds so the player can see the result before next round
            pygame.time.wait(5000)

            # Mark round as complete
            round_complete = True
            player_choice = None
            opponent_choice = None

        # Reset for next round
        if round_complete:
            round_complete = False  # Reset flag to indicate the next round can begin

        pygame.display.update()

        # Check if max rounds are reached
        if rounds >= max_rounds:
            SCREEN.fill(GRAY)  # Clear the screen just before displaying the results

            show_final_score(player_total_score, opponent_total_score)
            pygame.time.wait(6000)  # Wait for 6 seconds before resetting
            player_total_score, opponent_total_score, rounds = reset_game()


# Draws buttons for cooperating and defecting
def drawButtons():
    font = pygame.font.SysFont(None, 36)

    # Cooperate button
    cooperate_rect = pygame.Rect(WINDOW_WIDTH // 4 - BUTTON_WIDTH // 2, WINDOW_HEIGHT - 100, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(SCREEN, COOPERATE_COLOR, cooperate_rect, border_radius=BUTTON_RADIUS)
    pygame.draw.rect(SCREEN, BLACK, cooperate_rect, 3, border_radius=BUTTON_RADIUS)
    cooperate_text = font.render("Cooperate", True, BLACK)
    
    # Center the text on the button
    text_rect = cooperate_text.get_rect(center=(cooperate_rect.centerx, cooperate_rect.centery))
    SCREEN.blit(cooperate_text, text_rect)

    # Defect button
    defect_rect = pygame.Rect(3 * WINDOW_WIDTH // 4 - BUTTON_WIDTH // 2, WINDOW_HEIGHT - 100, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(SCREEN, DEFECT_COLOR, defect_rect, border_radius=BUTTON_RADIUS)
    pygame.draw.rect(SCREEN, BLACK, defect_rect, 3, border_radius=BUTTON_RADIUS)
    defect_text = font.render("Defect", True, BLACK)
    
    # Center the text on the button
    text_rect = defect_text.get_rect(center=(defect_rect.centerx, defect_rect.centery))
    SCREEN.blit(defect_text, text_rect)

    return cooperate_rect, defect_rect


# Function for simulating one round
def simulate_round(A_choice, B_choice):
    return payoff_matrix[(A_choice, B_choice)]

# Displays the result for a single round
def display_result(player_choice, opponent_choice, player_score, opponent_score):
    font = pygame.font.SysFont(None, 48)
    result_text = f"You chose {player_choice}, Opponent chose {opponent_choice}"
    score_text = f"You got: {player_score} points, Opponent got: {opponent_score} points"

    result_surface = font.render(result_text, True, BLACK)
    score_surface = font.render(score_text, True, BLACK)

    SCREEN.blit(result_surface, (WINDOW_WIDTH // 2 - result_surface.get_width() // 2, WINDOW_HEIGHT // 2 - 100))
    SCREEN.blit(score_surface, (WINDOW_WIDTH // 2 - score_surface.get_width() // 2, WINDOW_HEIGHT // 2))

# Displays the cumulative scores and rounds
def display_scores(player_total_score, opponent_total_score, rounds):
    font = pygame.font.SysFont(None, 36)
    score_text = f"Rounds: {rounds} | Your Total Score: {player_total_score} | Opponent's Total Score: {opponent_total_score}"
    score_surface = font.render(score_text, True, BLACK)
    SCREEN.blit(score_surface, (WINDOW_WIDTH // 2 - score_surface.get_width() // 2, 50))

# Shows the final score after all rounds
def show_final_score(player_total_score, opponent_total_score):
    font = pygame.font.SysFont(None, 40)
    final_text = f"Game Over! Final Score: You got {player_total_score} points - Opponent got {opponent_total_score} points"
    final_surface = font.render(final_text, True, BLACK)

    SCREEN.blit(final_surface, (WINDOW_WIDTH // 2 - final_surface.get_width() // 2, WINDOW_HEIGHT // 2 - 50))
    pygame.display.update()

# Resets the game state for a new game
def reset_game():
    return 0, 0, 0  # Reset player score, opponent score, and round count to zero


main()

```

## Länkar

- [Loggbok/Backlog]
- [Repository]
- [Rapport]

## Källor som kommer användas under arbetets gång

- [Prisoners Dilemma - Wikipedia](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)
- [Axelrods Tournament](https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/axelrod.html)
- [Tournaments — Axelrod 0.0.1 documentation](https://axelrod.readthedocs.io/en/fix-documentation/reference/overview_of_strategies.html)
- [The Evolution of Cooperation*](https://ee.stanford.edu/~hellman/Breakthrough/book/pdfs/axelrod.pdf)
- [Matplotlib documentation](https://matplotlib.org/stable/users/index.html)
- [The Prisoner’s Dilemma: A Mathematical Analysis](https://www.horacemann.org/uploaded/HoraceMann/Images/News/2011-2012_News/James_Ruben_--_original.pdf)
- [SciPy documentation](https://docs.scipy.org/doc/scipy/)

[Loggbok/Backlog]: https://docs.google.com/document/d/1yisuDjvD-EE_7QIu7x1w64V1gVMFPEqq9ytYGSEC3EA/edit
[Repository]: https://github.com/axellampp/Gymnasiearbete---Axel
[Fångarnas dilemma]: https://en.wikipedia.org/wiki/Prisoner%27s_dilemma
[The Evolution of Cooperation]: https://ee.stanford.edu/~hellman/Breakthrough/book/pdfs/axelrod.pdf
[Rapport]: https://docs.google.com/document/d/1bJazxY4JuGaCz19F5Xv1guXV4rf12aoBuNfNissQKZo/edit?tab=t.0
