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

fixed_line1 = 0
fixed_line2 = 0
mobile = 0
telemarketer = 0
for num in numbers:
    if num[1:4] == "080":
        fixed_line1 += 1
    elif num[1] == "0":
        fixed_line2 += 1
    elif num[0] == "7" or num[0] == "8" or num[0] == "9":
        mobile += 1
    elif num[:3] == "140":
        telemarketer += 1
dic = {"Fixed lines" : fixed_line1 + fixed_line2,
"Mobiles" : mobile,
 "Telemarkers" : telemarketer}

print("The numbers called by people in Bangalore have codes:")
print(dic)

per = fixed_line1/(fixed_line1 + fixed_line2 + mobile + telemarketer)
print("{0} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(per, 2)))


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
