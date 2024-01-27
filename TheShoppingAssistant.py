weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)
#used'==' for comparison
#added'else' after the second 'if' statement to handle the "cold" weather case

weather = input("Enter the weather: sunny, rainy, or cold: ")

if weather == "sunny":
    clothing = "sunglasses"
    accessory = "sunscreen"
elif weather == "rainy":
    clothing = "umbrella"
    accessory = "rain boots"
else:
    clothing = "sweater"
    accessory = "hat"

print(f"Recommended clothing: {clothing}")
print(f"Recommended accessory: {accessory}")
#the f before the string denotes an f-string, and it allows me to include variables or expressions directly inside the string