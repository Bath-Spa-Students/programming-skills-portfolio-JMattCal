#list your favorite fruits and then check if certain fruits are in the choices

# List of favorite fruits
favorite_fruits = ["apple", "banana", "strawberry", "mango", "grape"]

# Fruits to check
fruits_to_check = ["apple", "kiwi", "orange", "mango"]

print("My Favorite Fruits:")
for fruit in favorite_fruits:
    print(f"- {fruit}")

print("\nChecking Fruits:")
for fruit in fruits_to_check:
    if fruit in favorite_fruits:
        print(f"{fruit} is one of my favorite fruits.")
    else:
        print(f"{fruit} is not one of my favorite fruits.")
