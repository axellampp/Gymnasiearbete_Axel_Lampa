import random

### Poängsystem istället för belöning i fängelsetid då det är mest logiskt att vilja ha så mycket poäng som möjligt än fängelseår. Därmed är tabellen omvänd så logiken är lika.

payoff_matrix = {
    ("Cooperate", "Cooperate"): (3, 3),
    ("Cooperate", "Defect"): (0, 5),
    ("Defect", "Cooperate"): (5, 0),
    ("Defect", "Defect"): (1, 1),
}

# Funktion för en runda
def simulate_round(A_choice, B_choice):
    return payoff_matrix[(A_choice, B_choice)]
    
# Strategier
def always_cooperate(_):
    return "Cooperate"

def always_defect(_):
    return "Defect"

def random_strategy(_):
    return random.choice(["Cooperate", "Defect"])

# Börja med Cooperate, sedan kopiera motståndarens val.
def titfortat(lastOpponentMove=None):

    if lastOpponentMove is None:
        return "Cooperate"

    return lastOpponentMove

# Cooperate tills motståndaren har valt defekt, sen defekta alltid
def grim_strategy(lastOpponentMove=None):
    if grim_strategy.hasDefected:
        return "Defect"

    if lastOpponentMove == "Defect":
        grim_strategy.hasDefected = True
        return "Defect"
    
    return "Cooperate"    

grim_strategy.hasDefected = False


def simulate_tournament(num_rounds, A_strategy, B_strategy):
    A_score = 0
    B_score = 0

    last_move_A = None
    last_move_B = None

    for _ in range(num_rounds):
        A_choice = A_strategy(last_move_B)
        B_choice = B_strategy(last_move_A)

        outcome = simulate_round(A_choice, B_choice)

        A_score += outcome[0]
        B_score += outcome[1]

        last_move_A = A_choice
        last_move_B = B_choice
        
        # Debug
        # print(f"Player A chose to {A_choice}")
        # print(f"Player B chose to {B_choice}")

    
    print(f"Player A\'s score: ", A_score)
    print(f"Player B\'s score: ", B_score)


simulate_tournament(100, grim_strategy, titfortat)