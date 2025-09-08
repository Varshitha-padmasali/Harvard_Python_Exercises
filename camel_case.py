# implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
camel=input("camelCase: ")
snake=""
for char in camel:
    if char.isupper():
        snake=snake+"_"+char.lower()
    elif char.lower():
        snake=snake+char
print("snake_case:",snake)
