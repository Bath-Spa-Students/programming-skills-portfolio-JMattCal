#add whitespace and then remove using strip functions
# Add whitespace to a string
original_string = "Hello"
string_with_whitespace = "   " + original_string + "   "

# Remove the added whitespace using strip
stripped_string = string_with_whitespace.strip()

print("Original String:", original_string)
print("String with Whitespace:", string_with_whitespace)
print("Stripped String:", stripped_string)
