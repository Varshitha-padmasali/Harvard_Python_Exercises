# implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
mass=int(input("m: "))
c=300000000
energy=mass*(c**2)
print(energy)

