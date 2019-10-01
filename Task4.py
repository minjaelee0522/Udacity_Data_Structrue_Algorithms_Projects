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

n1 = set(numbers1 + numbers2 + numbers4)
n2 = set(numbers3)


tel = []
for num in n2:
    if num not in n1:
        tel.append(num)

print("These numbers could be telemarketers: ")
for i in sorted(tel):
    print(i)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

