#write a program that calcukates how many USB sticks she can buy and how much
# Get the price of a single USB stick and the total budget from the user
usb_stick_price = float(input("Enter the price of a single USB stick: $"))
total_budget = float(input("Enter your total budget: $"))

# Calculate how many USB sticks can be bought
num_usb_sticks = total_budget / usb_stick_price

# Calculate the total cost
total_cost = num_usb_sticks * usb_stick_price

# Print the results
print(f"You can buy {int(num_usb_sticks)} USB stick(s).")
print(f"The total cost will be: ${total_cost:.2f}")
