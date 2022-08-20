#Ex. Write a program which repeatedly reads numbers until the user types "done". Once "done" is entered, print out the total, count
#and average of the numbers, If the user enters anything other than a number, detect their mistake using try and ecvept and print out 
#an error message and skip to the next number

count = 0
total = 0.0
while True:
    user_input = input("Enter a number:")

    if user_input == "done":
        if count == 0:
            continue
        break


    try:
        user_input = float(user_input)
    except:
        print("Invalid input")
        continue

    ++count
    total = total + user_input

print (total, count, (total/count))
    






