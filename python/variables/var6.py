# Author: Harel Haram
# Date: 2026-02-21
# Description: Test the looping variables from Python

# FOR
# Loop Counter
for num in range(3, 13):
    print(num)

for i in range(1, 6):
    print("$" * i)

name = "arielaram"
for i in name:
    print(i)

addition = 0
subtraction = 0
for i in range(1, 6):
    addition = addition + i
    subtraction = subtraction - i
    print(f"The result of the addition is {addition}, while the result of the subtraction is {subtraction}")
