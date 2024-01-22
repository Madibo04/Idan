#A code to calculate the point of a football club in a league
#Getting input
won=int(input())
draw=int(input())
#Setting point for game win and game draw
winp=3
drawp=1
#Calculating total point
Tp=((won*winp)+(draw*drawp))
print(Tp)
