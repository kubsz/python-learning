#REG EX
import re
file = open("intro.txt")
for line in file:
    line = line.rstrip()
    if re.search("^the ", line):
        print (line)


# find dates within a sentence

import re
sentence = "My available dates for a meeting are 22 August 2022 and 09 October 22"
dates = re.findall("[0-9]+\s[A-Za-z]+\s[0-9]+", sentence)
print(dates)

email = "From: kubs@kubs.uk The timestamps are as follows: 09:21 AM and 16:54 PM on 23 Jan 2021"
time = re.findall("[0-9]+:[0-9]+\s\S+", email)
print(time)

email_add = "lyla@cranberrypanda.co.uk, pitajenlyla@gmail.com, and kubs@kubs.uk"
host = re.findall("@(\S+[^,])", email_add)
print(host)

