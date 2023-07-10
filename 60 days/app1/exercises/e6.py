# write a program that Asks the user for input "Add a new member" and then adds this into file members.txt existing in this same folder

# Path: 60 days\app1\bonus\bonus7.py
# Compare this snippet from 60 days\app1\bonus\bonus6.py:
data = input("Enter a new member: ") + "\n"

file = open("members.txt", "a")
file.write(data)
file.close()
#
