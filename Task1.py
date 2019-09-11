"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

numbers1 = []
numbers2 = []
for number in texts:
    numbers1.append(number[0])
    numbers2.append(number[1])


numbers3 = []
numbers4 = []
for number in calls:
    numbers3.append(number[0])
    numbers4.append(number[1])

numbers = set(numbers1 + numbers2 + numbers3 + numbers4)

print("There are {0} different telephone numbers in the records.".format(len(numbers)))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
