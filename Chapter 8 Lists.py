#go through the each line of the file, print out email address in that file, store the email address in a list

#file_name = input("Enter file name:")
file_name = 'mbox-short.txt'
file = open(file_name)
email_list = list()
for line in file:
    line =line.rstrip()
    blocks = line.split()
    for block in blocks:
        if "@" in block:
            email_list.append(block)
print(email_list)
