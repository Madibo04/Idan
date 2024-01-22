class Person:
     def __init__(self, a, b):
        self.name = a
        self.score = b
     def __str__(self):
        return (f"I am {self.name} and my score is {self.score}%.")
    
     def greet(self):
        return f"Hello from {self.name}"
    
     def print_score(self):
        return f"My score is {self.score}%."