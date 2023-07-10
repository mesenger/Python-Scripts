date = input("Enter today's date: ")
mood = input("Rate your mood from 1 to 10: ")
thoughts = input("What are you thinking?\n")

with open(f"..\\journal\\{date}.txt", "w") as file:
    file.write(f"Mood: {mood}\n")
    file.write(f"Thoughts: {thoughts}\n")