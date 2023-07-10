feet_inches = input("Enter the number of feet and inches, separated by a space: ")

def parse_feet_and_inches(feet_inches):
    """Parse feet and inches from a string.
    
    Args:
        feet_inches (str): A string containing feet and inches.
        
    Returns:
        dict: A dictionary containing feet and inches.
    """
    feet_inches = feet_inches.split()
    feet = float(feet_inches[0])
    inches = float(feet_inches[1])
    return {"feet": feet, "inches": inches}


def convert(parsed):
    """Convert feet and inches to centimeters.

    Args:
        parsed (dict): A dictionary containing feet and inches.

    Returns:
        float: The number of centimeters.
    """
    centimeters = parsed["feet"] * 30.48 + parsed["inches"] * 2.54
    return centimeters

parsed = parse_feet_and_inches(feet_inches)
print(parsed)

result = convert(parsed)

print(f"{parsed['feet']} feet and {parsed['inches']} inches is {result} centimeters.")


#print(convert(feet_inches))