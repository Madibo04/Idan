names = []

def get_name():
    inp = input("Name: ").strip()
    names.append(inp)


def print_name():
    print ("Adieu, adieu, to ", end="")
    if len(names) == 1:
        print(names[0])
        return
    if len(names) == 2:
        print(f"{names[0]} and {names [1]}")
        return
    for index, name in enumerate(names):
        if index != len(names) - 1:
            print(f"{name}, ", end="")
        else:
            print(f"and {name}")


while True:
    try:
        get_name()
    except EOFError:
        print_name()
        break