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

times = []
for i in calls[1379:1577]:
    times.append(int(i[3]))

print(times)
idx = calls.index(max(times))

print(idx)





print("{0}, {1} spent the longest time, {2} seconds, on the phone during September 2016.".format(calls[idx][0], calls[idx][1], calls[idx][3]))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

