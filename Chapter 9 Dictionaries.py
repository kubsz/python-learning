file_name = input("Enter file name:")
file = open(file_name)

word_count = {}
for line in file:
    words = line.split()
    for word in words:
        word_count[word] = word_count.get(word,0) + 1


bigcount = 0
bigword = None
for word,count in word_count.items():
    if count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)

