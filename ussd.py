import time
import sys

def home():
    print("\033c")
    print("Welcome User")
    print("1. Borrow Credit")
    print("2. Borrow Data")
    print("3. Check Balance")
    print("0. Quit")
    response = input().strip()
    try:
        response = int(response)
    except ValueError:
        print("Invalid Option")
        time.sleep(2)
        home()
    if response not in [0,1,2,3]:
        print("Invalid Option")
        time.sleep(2)
        home()
    match response:
        case 1:
            credit()
        case 2:
            data()
        case 3:
            balance()
        case 0:
            quit()

def quit():
    print("\033c")
    print("Thank you for choosing HiiT Network.")
    sys.exit()

def balance():
    print("\033c")
    print("Your balance is N2000.00 only.")
    print()
    print("1 Back")
    print("0 Quit")
    res = input().strip()
    if res not in ["1", "0"]:
        print("Invalid Option")
        time.sleep(2)
        balance()
    if res == "1":
        home()
    quit()

def assurance(a, b):
    print("\033c")
    print(f"Do you want to proceed with {a}?")
    print("1. Accept")
    print("2. Cancel")
    print("9. Main Menu")
    res = input().strip()
    if res not in ["1", "2","9"]:
        assurance(a, b)
    if res == "1":
        print("\033c")
        print(f"You have been credited {a} only")
        input("Enter any key to go back ")
        home()
    if res == "2":
        if b == 1:
            data()
        else:
            credit()
    if res == "9":
        home()

# def credit_assurance(a):
#     print("\033c")
#     print(f"Do you want to proceed with {a}?")
#     print("1. Accept")
#     print("2. Cancel")
#     print("9. Main Menu")
#     res = input().strip()
#     if res not in ["1", "2","9"]:
#         assurance(a)
#     if res == "1":
#         print("\033c")
#         print(f"You have been credited {a} only")
#         input("Enter any key to go back ")
#         home()
#     if res == "2":
#         credit()
#     if res == "9":
#         home()

def data():
    print("\033c")
    print("You are eligible to borrow the following")
    print("1. 1GB/N250")
    print("2. 10GB/N2000")
    print("3. 25GB/N4000")
    print("4. 50GB/N8000")
    print()
    print("0. Back")
    print("9. Quit")
    res = input().strip()
    if res not in ["1", "2", "3", "4", "0", "9"]:
        print("Invalid Option")
        time.sleep(2)
        data()
    if res == "9":
        quit()
    elif res == "0":
        home()
    elif res == "1":
        assurance("1GB/N250", 1)
    elif res == "2":
        assurance("10GB/N2000", 1)
    elif res == "3":
        assurance("25GB/N4000", 1)
    elif res == "4":
        assurance("50GB/N8000", 1)

def credit():
    print("\033c")
    print("You are eligible to borrow up to N2000")
    print("1. N100")
    print("2. N200")
    print("3. N500")
    print("4. N1000")
    print("5. N2000")
    print()
    print("0. Back")
    print("9. Quit")
    res = input().strip()
    if res not in ["1", "2", "3", "4", "5", "0", "9"]:
        print("Invalid Option")
        time.sleep(2)
        credit()
    if res == "9":
        quit()
    elif res == "0":
        home()
    elif res == "1":
        assurance("N100", 2)
    elif res == "2":
        assurance("N200", 2)
    elif res == "3":
        assurance("N500", 2)
    elif res == "4":
        assurance("N1000", 2)
    elif res == "5":
        assurance("N2000", 2)

try:
    home()
except KeyboardInterrupt:
    print("\033c")
    print("Good bye")