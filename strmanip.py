# Gavin Howard
# 2/10/2020
# String Manipulation

print("Please enter a string with no less than 3 words.")
user_string = input("> ")
print("There are " + str(len(user_string)) + " characters in your string.")
print(user_string[0] + " is the first letter of your string.")
print(user_string[-1] + " is the last character of your string")
print("This is what your sting looks like capitalized: " + user_string.upper())
print("This is your string in title case: " + user_string.title())
print("Here your string is broken down into individual words: " + str(user_string.split(' ')))
print("Here is your string five times: " + user_string * 5)
print("Now I am going to replace the third character in your string.")
print(user_string.replace(user_string[2], ' ', 1))
print("Your string is composed solely of characters, no numbers or characters: " + str(user_string.isalpha()))
