#Ex 1: Rewrite your pay computation to give the employee 1.5 times 
# the hourly rate for hours worked over 40 hours

# hours = float(input("Enter Hours: "))
# rate = float(input("Enter Rate: £"))
# othours = hours - 40
# otrate = 1.5 * rate
# if hours <= 40:
#     pay = hours * rate
#     pay = round(pay,2)
#     print ("Pay:£ ",pay)
# else:
#     pay = (40 * rate) + (othours * otrate)
#     pay = round(pay, 2)
#     print("Pay:£ ", pay)

#Ex.2 - Print an error message when a non-numeric input is written
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: £"))
except:
    print ("Error, please enter a numeric input")
    quit()
othours = hours - 40
otrate = 1.5 * rate
if hours <= 40:
    pay = hours * rate
    pay = round(pay,2)
    print ("Pay:£ ",pay)
else:
    pay = (40 * rate) + (othours * otrate)
    pay = round(pay, 2)
    print("Pay:£ ", pay)
