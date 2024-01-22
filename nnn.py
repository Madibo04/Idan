num = input("Enter a number: \n").strip()
num = int (num)
i = 2
while i < num:
    if i % 2==0:
        print(i)
    i +=1
# for i in range(2,num+2):
#     print (i)
# def division(i,j):
#     return i/j
# division(2, 1)