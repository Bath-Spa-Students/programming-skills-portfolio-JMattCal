def identify_alien_color(color):
    alien_colors = ['green', 'yellow', 'red']

    if color.lower() in alien_colors:
        return f"The alien's color is {color.lower()}!"
    else:
        return "This doesn't seem to be an alien color."

# Example usage:
alien_color = input("Enter the alien's color: ")
result = identify_alien_color(alien_color)
print(result)

