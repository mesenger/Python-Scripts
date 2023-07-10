import csv

with open('weather.csv', 'r') as file:
    reader = list(csv.reader(file))

#print(reader)

city = input('Enter city name: ')

for row in reader:
    if row[0] == city:
        print(row[1])
        break
        
