s = int(input("Enter the total number of Student"))

score = []
for i in range(0, s, 1):
    score.append(0)

for i in range(0, s, 1):
    score[i] = float(input("Enter score for the student no. %d>" % (i + 1)))
