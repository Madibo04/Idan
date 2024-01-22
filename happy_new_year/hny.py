# # while True:
# #     name = input("Enter your name: ").strip()
# #     score = input("Enter your score: ").strip()
# #     if name == "" or score == "":
# #         break
# #     with open("score.csv", "a") as file:
# #         line = name + "," + score + "\n"
# #         file.write(line)

# # try:
# #     with open("score.csv") as file:
# #         for line in file:
# #             line = line.rstrip()
# #             name,score = line.split(',')
# #             print(f"{name} scored {score}")
# # except FileNotFoundError:
# #     pass

# with open("names.txt" , "r") as file:
#     for ln in sorted(file, reverse=True):
#         print(ln.rstrip())
import json

my_record = {"name": "Adebola",
             "gender" : "Female",
             "graduate" : True,
             "age" : 27
             }
with open("record.json" , "w") as file:
    json.dump(my_record, file)