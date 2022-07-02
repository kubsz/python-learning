# def greet(lang):
#     if lang == "English":
#         print("Hello!")
#     elif lang == "Spanish":
#         print("Hola!")
#     elif lang == "French":
#         print("Bonjour!")

# lang = input("Enter language:")
# greet(lang)

#Ex. 6 - Rewrite your pay computation with time and a half for overtime and 
# create a function called computepay which takes two parameters (hours and pay)

# def computepay (hours,rate):
#     hours = float(hours)
#     rate = float(rate)
#     othours = hours - 40
#     otrate = 1.5 * rate
#     if hours <= 40:
#         pay = hours * rate
#         pay = round(pay,2)
#         print ("Pay:£ ",pay)
#     else:
#         pay = (40 * rate) + (othours * otrate)
#         pay = round(pay, 2)
#         print("Pay:£ ", pay)

# computepay(56,10)

#Ex. 7 - Write a function called computegrade that takes a score as its parameter 
# and returns a grade as a string

def computegrade(score):
    if score >= 0.9:
        print ("Grade:A")
    elif score == 0.8:
        print ("Grade:B")
    elif score == 0.7:
        print ("Grade:C")

computegrade(0.7)
