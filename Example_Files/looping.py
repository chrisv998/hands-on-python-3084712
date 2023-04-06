#Looping File example: LinkedIn course

NAMES = ["Chris", "Jake", "John", "Mary"]
AGES = [20, 21, 22, 23]

for name in NAMES:
    print(name)



for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for i, name in enumerate(NAMES):
    print(f"{i} {name}")