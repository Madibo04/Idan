#Creating an array of elements
A = [19, 22, 23, 47, 56, 35, 54, 62, 76, 45, 88]
#Indicating the even indices in the list
Evens=A[0::2]
print (Evens)
#Sum of even indexes
sum=0
for counter in range(0, len(A),2):
    sum = sum + A[counter]
print(sum)
#Calculating mean
Average=(A[4] + A[6] + A[8] + A[10] / 4)
print (Average)
