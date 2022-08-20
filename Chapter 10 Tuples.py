file_name = input("Enter file name:")
file = open(file_name)

word_count = {}
for line in file:
    words = line.split()
    for word in words:
        word_count[word] = word_count.get(word,0) + 1

#print(word_count)

tup = list()
for (key,value) in word_count.items():
    tup.append((value,key))
tup = sorted(tup, reverse=True)

# for i in tup:
#     print (i)

# find top 10 most commonly used words in the file
for i in tup[:10]:
    print (i)

