#basketball game if-elif-else statement

import random

# Set the player's shooting percentages for different shot types
layup_percentage = 70
jump_shot_percentage = 50
three_point_percentage = 35

# Generate a random number to simulate the player's shot
shot_result = random.randint(1, 100)

print("Welcome to the Basketball Game!")
print("You are about to take a shot.")

shot_type = input("Choose your shot type (layup/jump shot/three-point): ")

if shot_type == "layup":
    if shot_result <= layup_percentage:
        print("You made the layup! Two points for your team.")
    else:
        print("Oh no, you missed the layup.")
elif shot_type == "jump shot":
    if shot_result <= jump_shot_percentage:
        print("Swish! You made the jump shot. Two points for your team.")
    else:
        print("Your jump shot missed the mark.")
elif shot_type == "three-point":
    if shot_result <= three_point_percentage:
        print("It's good! You made the three-point shot. Three points for your team.")
    else:
        print("The three-point attempt falls short.")
else:
    print("Invalid shot type. Please choose 'layup', 'jump shot', or 'three-point'.")



