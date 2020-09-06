import random

random.seed(12)

dm = ["daren", "meghan"]
bn = ["brendan", "nick"]
rest = ["Garrett", "Ben_Bailey", "Kris", "Ed"]


print("Meghan vs. Daren: %s wins" % random.choice(dm))
print("Brendan vs. Nick: %s wins" % random.choice(bn))

for i in range(4):
    choice = random.choice(rest)
    print(choice)
    rest.pop(rest.index(choice))
