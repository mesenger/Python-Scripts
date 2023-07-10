waiting_list = ['John', 'Mary', 'Peter', 'David', 'Marry', 'Henry', 'Tom']
waiting_list.sort()
for index, name in enumerate(waiting_list):
    print(f"{index + 1}.{name.capitalize()}")
# Compare this snippet from 60 days\app1\experiments\e1.py:

filenames = ['document', 'report', 'presentation']
for index, filename in enumerate(filenames):
    print(f"{index}-{filename.capitalize()}.txt")