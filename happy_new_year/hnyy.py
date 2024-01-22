import json
# # record = [['Titilope', 82],
# #           ['James', 75],
# #           ['Lincoln', 20]
# # ]
# # with open ('score.csv', 'a') as file:
# #     writer = csv.writer(file, delimiter='*', lineterminator="\n")
# #     writer.writerows(record)
# # with open('score.csv', 'r') as file:
# #     reader = csv.DictWriter(file)
# #     for row in reader:
# #         print(row)
# with open('score.csv', 'a') as file:
#     names = ['name', 'score']
#     writer = csv.DictWriter(file, fieldnames=names)
#     writer.writerow({'name': 'Bolu', 'score':78})
# my_data = {"name" : "Ade", "married" : True, "age" : 33}
with open("data.json", 'r') as file:
    result=json.load(file)
    print(result)