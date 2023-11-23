#you only have space for 2 guests, print a new message saying only can be invited

# Create the initial guest list
guest_list = [
    "Albert Einstein",
    "Maya Angelou",
    "Nelson Mandela",
    "Audrey Hepburn",
    "Leonardo da Vinci",
    "Steve Jobs",
    "Marie Curie",
    "George Orwell",
    "Winston Churchill",
    "Amelia Earhart"
]

# Print the initial guest list
print("Guest List for the Dinner Party:")
for guest in guest_list:
    print(guest)

# Check if there is space for more guests
if len(guest_list) < 2:
    print("Only two guests can be invited.")
else:
    # If a guest can't make it, replace them with a new guest
    guest_to_replace = "Audrey Hepburn"
    new_guest = "Frida Kahlo"

    if guest_to_replace in guest_list:
        index = guest_list.index(guest_to_replace)
        guest_list[index] = new_guest
        print(f"\n{guest_to_replace} can't make it, so {new_guest} has been invited instead.")

    # Print the updated guest list
    print("\nUpdated Guest List:")
    for guest in guest_list:
        print(guest)
