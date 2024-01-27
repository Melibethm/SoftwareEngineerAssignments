attendees = int(input("Enter number of attendees: "))  
venue = "large hall" 
if attendees > 100 
else "conference room"
print(venue)
# Convert input to integer

# Task 2: Additional Facilities
attendees = int(input("Enter number of attendees: "))  # Convert input to integer
venue = "large hall" if attendees > 100 else "conference room"

# Recommend additional facilities
if attendees > 50:
    print("Consider adding an audio system for better experience.")
if attendees > 80:
    print("You may also consider providing a projector for presentations.")

# Task 3: Catering Choices
catering_choice = input("Do you want vegetarian food? (yes/no): ").lower()

# Recommend catering based on user's choice
if catering_choice == "yes":
    print("We recommend Veggie Delight Caterers for vegetarian options.")
else:
    print("We recommend Gourmet Meals Caterers for a variety of catering options.")

print(f"The event will be held in the {venue}.")
