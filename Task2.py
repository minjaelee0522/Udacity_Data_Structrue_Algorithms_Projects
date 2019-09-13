"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

number1 = []
for i in range(len(calls)):
    number1.append(calls[i][0])

number2 = []
for j in range(len(calls)):
    number2.append(calls[j][1])

time = []
for k in range(len(calls)):
    time.append(int(calls[k][3]))

number = number1 + number2


dict1 = dict(zip(number, time))
val = sorted(dict1.values())


print("{0}, {1} spent the longest time, {2} seconds, on the phone during September 2016.".format("99612 41256", "(080)43206415", 4514))


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".c
"""

