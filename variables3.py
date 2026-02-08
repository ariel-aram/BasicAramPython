# Author: Harel Haram
# Date: 2026-02-07
# Description: Calculate gas pricing

gasPrice = 1.50
ethanolPrice = 1.20
division = ethanolPrice / gasPrice
currency = "USD"

soberanoBolivar = 381.68
bolivar = "VES"

conversionGAS = soberanoBolivar * gasPrice
conversionETH = soberanoBolivar * ethanolPrice

# The f variable was not learned in the course, but I found it thanks to Windsuus autocompletion feature
# I'M NOT VIBE CODING, YOU PUNKS
print(
    f"The price of the oil that you pump for money in the middle east and turn into a rich boi: {gasPrice} {currency}"
)
print(f"As well as the price of your silly ethanol: {ethanolPrice} {currency}")
print(
    f"Conversion to the most unvalued currency in the whole observable universe: Gas {conversionGAS} {bolivar} | Ethanol {conversionETH} {bolivar}"
)
print("Your money is worth nothing.")
