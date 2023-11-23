#alien game if statement

# Alien game

print("You have encountered an alien!")
print("It is a small, green alien with multiple eyes.")

choice = input("What will you do? (shoot/hug/run) ")

if choice == "shoot":
    print("You shoot the alien. Good job! You win.")
elif choice == "hug":
    print("You hug the alien. It turns out to be a friendly alien. You win.")
elif choice == "run":
    print("You run away from the alien. It chases you, and you escape. You win.")
else:
    print("You hesitate, and the alien gets bored and leaves. You win.")
