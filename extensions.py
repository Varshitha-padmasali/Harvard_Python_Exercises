# implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

inp=input("File name:")
fl=inp.lower()
fl=fl.strip()
if fl.endswith(".gif"):
    print("image/"+"gif")
elif fl.endswith(".jpg"):
    print("image/"+"jpeg")
elif fl.endswith(".jpeg"):
    print("image/"+"jpeg")
elif fl.endswith(".png"):
    print("image/"+"png")
elif fl.endswith(".pdf"):
    print("application/"+"pdf")
elif fl.endswith(".txt"):
    print("text/"+"plain")
elif fl.endswith(".zip"):
    print("application/"+"zip")
else:
    print("application/octet-stream")
