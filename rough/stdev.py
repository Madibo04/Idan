print("This program computes the mean and standard deviation of some data")
n=int(input("Enter the total number of data"))
#Declaring the array or list
score=[]
for i in range(0, n, 1):
    score.append(0)

#Append data into the list
for i in range(0, n, 1):
    #k=i+1
    score[i]= float(input("Enter score for the student no. %d>" %(i+1)))

#Summing the data altogether
sum = 0
for i in range (0, n, 1):
    sum +=score[i]

#Computing the Mean
mean=sum/n
from math import sqrt

#Computing the standard deviation
var=0
for i in range(0, n, 1):
    var+=((score[i]-mean)**2)/n

stdev = sqrt(var)

print("Sum of data = ", sum)
print("The mean = ", mean)
print("Standard Deviation= ", stdev)
