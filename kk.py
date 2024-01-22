# def calculator(x, y, z):
#     if y == "+":
#         return x + z
#     if y == "-":
#         return x - z
#     if y == "*":
#         return x * z
#     if y == "/":
#         return x / z
#     if y == "**":
#         return x ** z
#     return
# a = int(input())
# b = int(input())
# c = int(input())

# a_square = calculator(a,"**", 2)
# b_square = calculator(b, "**", 2)
# last_part = calculator(a,"*", c)
# last_part = calculator(last_part, "*", 2)
# first_addition = calculator (a_square, "+", b_square)
# final_addition = calculator(first_addition, "+", last_part)
# print(final_addition)
# i = 1
# while i < 101:
#     if i % 15 == 0:
#         print ("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)
#     i += 1
def fizzbuzz(a, b):
    while a <= b:
        if a % 15 == 0:
            print("FizzBuzz")
        elif a % 5 == 0:
            print("Buzz")
        elif a % 3 == 0:
            print("Fizz")
        else:
            print(a)
        a +=1
a = int(input("Enter Starting point "))
b = int(input("Enter Endpoint "))

fizzbuzz(a, b)