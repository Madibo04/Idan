from tc import Person


def test_greet():
    n_person = Person("Mr C", 78)
    assert n_person.greet() == "Hello from Mr C"
    assert n_person.print_score() == "My score is 78%."

def test_fullname():
    student = Person("Adetola", 85)
    assert student.__str__() == "I am Adetola and my score is 85 "