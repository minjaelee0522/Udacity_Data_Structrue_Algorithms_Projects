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

numbers = set()

for number in texts:
    numbers.add(number[0])
    numbers.add(number[1])

for number in calls:
    numbers.add(number[0])
    numbers.add(number[1])

answer = len(numbers)

print("There are {0} different telephone numbers in the records.".format(answer))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
