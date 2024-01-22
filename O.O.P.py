class Person:
    x = 7
    y = 5
    def __init__(self, a, b):
        self.name = a
        self.age = b
    def __str__(self):
        return (f"I am {self.name} and I am {self.age} years old")
    
    def greet(self):
        print(f"Hello from {self.name}")
        return "How are you"
    
    def print_age(self):
        print (f"I {self.age} years old.")
        return "Thank you"
    

p1 = Person("Tom", 15)
p2 = Person("Tim", 21)

print(p1)
print(p2)

print(p1.greet())
print(p2.print_age)