#write a python program which accepts the radius of a circle from the user
import math

# Accept the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * (radius ** 2)

# Print the result
print(f"The area of the circle with radius {radius} is: {area:.2f}")