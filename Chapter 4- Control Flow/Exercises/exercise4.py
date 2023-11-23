#if-elif-else statement for variable age

# Get the age from the user
age = int(input("Please enter your age: "))

if age < 18:
    print("You are a minor.")
    print("You cannot vote or purchase alcohol.")
elif age >= 18 and age < 21:
    print("You are of legal age but not yet 21.")
    print("You can vote but cannot purchase alcohol.")
else:
    print("You are an adult.")
    print("You can vote and purchase alcohol.")
