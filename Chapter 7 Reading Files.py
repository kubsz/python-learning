#Ex.1 - Write a program to read through a file and print the contents of the file
#line by line in upper case

# file_name = input("Enter a file name:")
# file = open(file_name)
# file_content = file.read()
# print(file_content.upper())

#Ex. 2 - User enters file name, open file, count how many characters in each line and print the line with the most characters


def Find_line_w_most_characters(file):
    highest_line_content = ' '
    for line in file:
        line = line.rstrip()
        if len(line) > len(highest_line_content):
            highest_line_content = line
    print(highest_line_content, len(highest_line_content))

while True:
    file_name = input("Enter file name:")
    try:
        file = open(file_name)
        break
    except:
        print("File cannot be found")
        continue
Find_line_w_most_characters(file)


