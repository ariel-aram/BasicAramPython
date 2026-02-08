# Author: Harel Haram
# Date: 2026-02-07
# Description: Convert Celsius to Fahrenheit and Kelvin

celsius = int(input("Input the temperature of ur booze: "))
fahrenheitDivision = 9 / 5
kelvinAddition = 273.15
fahrenheitAdition = 32

fahrenheit = celsius * fahrenheitDivision + fahrenheitAdition
kelvin = celsius + kelvinAddition

print(
    "The temperature of your booze is",
    fahrenheit,
    "°F and",
    kelvin,
    "K. Enjoy your boozing day with ur homies like the lame ahh booze you are.",
)
