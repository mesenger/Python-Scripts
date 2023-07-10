feet_inches = input("Enter the number of feet and inches, separated by a space: ")

def convert(feet_inches):
    feet_inches = feet_inches.split()
    feet = int(feet_inches[0])
    inches = int(feet_inches[1])
    centimeters = feet * 30.48 + inches * 2.54
    return centimeters

print(convert(feet_inches))