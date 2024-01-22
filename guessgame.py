from random import randint

n = 0
def get_level():
    global n
    try:
        n = int(input("Level: "))
    except ValueError:
        get_level()
    else:
        if n < 1:
            get_level()
        else:
            play()

def play():
    com = randint(1, n)
    while True:
        user = guess()
        if user < com:
            print("Too Small!")
        elif user > com:
            print("Too Large!")
        else:
            print("Just right!")
            break

def guess():
    try:
        n = int(input("Guess: "))
    except ValueError:
        return guess()
    else:
        if n < 1:
            return guess()
        else:
            return n



get_level()