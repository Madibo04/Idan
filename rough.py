import random
# # while True:
# #     x = input("Enter a number, 0 to break ").strip()
# #     if x == "0":
# #         print ("Thank you.")
# #         break
# #     print("You typed " + x)
# a = 10
# while a < 51:
#     if a % 3 == 0:
#         a+=1
#         continue
#     print(a)
#     a+=1
# names = []
# print ("Enter the names of your classmates, 0 to cancel.")
# while True:
#     x=input("Enter a name ").strip()
#     if x =="0":
#         break
#     names.append(x)
# if len(names) > 0:
#     if len(names) == 1:
#         print("The name of your classmate is: ")
#     else:
#         print("The names of your classmates are ")
#         for i in names:
#             print (i)
# n = int(input())

# for x in range(1, n, 2):
#     if x % 3 == 0 and x % 5 == 0:
#         print("SoloLearn")
#     elif x % 3 == 0:
#         print("Solo")
#     elif x % 5 == 0:
#         print("Learn")
#     else:
#         print(x)

# random.seed(int(input()))
# for i in range(7):
#     dice1 = random.randint(1, 6)
# for i in range(7):
#     dice2 = random.randint(1, 6)

# print(dice1)
# print(dice2)
# def print_nums(x):
#     res = 0
#     for i in range(x):
#         res +=i
#     return res
# print(print_nums(4))
celsius = int(input())

def conv(x):
    return 9/5 * x + 32
fah = conv(celsius)
print(fah)