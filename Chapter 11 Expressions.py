#REGEX
import re
file = open("intro.txt")
for line in file:
    line = line.rstrip()
    if re.search("^the ", line):
        print (line)