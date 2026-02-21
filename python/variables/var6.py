# Author: Harel Haram
# Date: 2026-02-21
# Description: Test the looping variables from Python

# FOR
# Loop Counter
for num in range(3, 13):
    print(num)

print("======")

for i in range(1, 6):
    print("$" * i)

print("======")

name = "arielaram"
for i in name:
    print(i)

print("======")

addition = 0
subtraction = 0
for i in range(1, 6):
    addition = addition + i
    subtraction = subtraction - i
    print(
        f"The result of the addition is {addition}, while the result of the subtraction is {subtraction}"
    )

print("======")

team = ["Ariel", "Metro", "Aditya", "Bloxy", "Ahmed", "Lore", "Scorpion"]
print(team)
