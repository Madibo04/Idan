name = input("What is your full-name? \n").strip().title()
age = int(input("How old are you? \n").strip())
if age >=18: print ("You are Welcome " + name)
else: print (f"Sorry {name}, you are not eligible.")
