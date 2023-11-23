#one of your guests cant make it, print the name of the guest and invite a new one

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
