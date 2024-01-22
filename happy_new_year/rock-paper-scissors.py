import random
from time import sleep
options = ["R", "P", "S"]

def prompt():
    picked = input("Enter an option: ").strip().upper()
    if picked not in options:
        print("Wrong input")
        return prompt()
    return picked

def start():
    print('\033c')
    print("Welcome to Rock-Papper-Scissors Game")
    print("To play, Enter\nR to Rock\nP for Papper\nS for Scissors")
    input("Enter any key to continue: ")
    round()


def round():
    round, comp, user = 1, 0, 0
    while (round <= 5 and abs(comp - user) < 3):
        if  (round == 5 and abs(comp - user) > 1):
            break
        score = play(round, comp, user)
        if score == 1:
            user += 1
        else:
            comp += 1
        round += 1
    if comp > user:
        winner = "Com"
    else:
        winner = "You"
    print('\033c')
    print("=========================================")
    print("==                                    ===")
    print("==                                    ===")
    print("==             GAME OVER              ===")
    print("==                                    ===")
    print(f"==          {winner}   Won                 ===")
    print("==                                    ===")
    print("==                                    ===")
    print("==                                    ===")
    print(f"==   comp {comp}             You {user}         ===")
    print("==                                    ===")
    print("==                                    ===")
    print("=========================================")


def play(round, computer, player):
    print('\033c')
    print("=========================================")
    print("==                                    ===")
    print("==                                    ===")
    print(f"==           ROUND {round}                  ===")
    print("==                                    ===")
    print("==                                    ===")
    print(f"==  comp  {computer}               You {player}       ===")
    print("==                                    ===")
    print("==                                    ===")
    print("=========================================")

    comp = random.choice(options)
    user = prompt()
    winner = -1
    if comp == user:
        print(f"Tie!")
        sleep(2)
        return play(round, computer, player)
    if comp == "R" and user == "P":
        print("You win!")
        winner = 1
    elif comp == "P" and user == "R":
        print("You lose!")
        winner = 0
    elif comp == "R" and user == "S":
        print("You lose!")
        winner = 0
    elif comp == "S" and user == "R":
        print("You win!")
        winner = 1
    elif comp == "S" and user == "P":
        print("You lose!")
        winner = 0
    elif comp == "P" and user == "S":
        print("You win!")
        winner = 1
    sleep(2)
    return winner



if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        print('\033c')
        print("Good bye!!")