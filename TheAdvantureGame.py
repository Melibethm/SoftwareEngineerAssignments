place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
#Used == for equality comparison in if conditions.
#Corrected the else to elif for the second condition inside the forest block.
#Removed unnecessary conditions after else.


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass  # Default path for invalid choices in the forest
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You can see a hidden passage!")
    elif action == "proceed in the dark":
        print("You stumbled upon a mysterious relic!")
    else:
        pass  # Default path for invalid choices in the cave
else:
    pass  # Default path for invalid choices in the initial place

#Added an additional input and decision-making block for the "cave" scenario.
#Used == for equality comparison in if conditions.
#Added a default pass statement for handling invalid choices at different points in the game.