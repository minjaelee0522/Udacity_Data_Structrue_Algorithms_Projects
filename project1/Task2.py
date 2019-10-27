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


records = {}
for call in calls:
    if call[0] in records:
        records[call[0]] += int(call[3])
    else:
        records[call[0]] = int(call[3])
    if call[1] in records:
        records[call[1]] += int(call[3])
    else:
        records[call[1]] = int(call[3])

longest = max(records, key=lambda i:records[i])
print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(longest, records[longest]))


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".c
"""

