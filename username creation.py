import random

def get_details():
    fn = input("Enter your first name: \n").strip()
    ln = input("Enter your last name: \n").strip()
    mn = input("Enter your middle name: \n").strip()
    # if not isinstance(fn, str) or (ln, str) or (mn, str):
    #     raise TypeError("Invalid input")
    full_name = []
    full_name.append(fn)
    full_name.append(ln)
    full_name.append(mn)
    username =  random.choice (full_name)    

    

#     return[fn, ln, mn]


# print (username)