class Person:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError("Name must be a str")
        if len(name) < 3:
            raise ValueError("Name must be 3 characters")
        if not isinstance(age, int):
            raise TypeError("Expecting an integer")
        if age < 1:
            raise ValueError("Age must not be less than one")
        self.name = name
        self.age = age
n_person = Person("Sam", 5)
print(n_person.age)
n_person.age = "Five"
print(n_person.age)