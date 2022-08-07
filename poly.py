class Man:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Привет! Я человек {self.name}!")

class Worker(Man):
    def greet(self):
        print(f"Привет! Я работник {self.name}!")

class Programmer(Worker):
    def greet(self):
        print(f"Привет! Я программист {self.name}!")

a = Man("Valera")
b = Worker("Ivan")
c = Programmer("Petr")

people = []

people.append(a)
people.append(b)
people.append(c)

a.greet()
b.greet()
c.greet()

print("------------")

for person in people:
    person.greet()












#b._B__private()
