#  implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
    
text=input("Input: ")
vowels="aeiouAEIOU"
result=""
for char in text:
    if char not in vowels:
        result=result+char
print("Output:",result)
