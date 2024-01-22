print("welome to ABC Bank of Nigeria")
for i in range (3):
    acct_no=6173517337
    acct_balance=10000
    pin_no=17123
    acct_no_request=int(input("enter your account number"))
    pin_no_request=int(input("enter your pin no"))
    if acct_no_request==acct_no and pin_no_request==pin_no:
        print('''
                               MAIN MENU
                           1. VIEW MY BALANCE
                           2. WITHDRAW CASH
                           3. DEPOSIT FUNDS
                           4. EXIT
                                                  ''')
        break
    else:
        Attempts='Attenmpt',i+1
        print(Attempts)
        if Attempts != "Attempt, 3":
            print("Re-enter")
        else:
            print("Log Out")
