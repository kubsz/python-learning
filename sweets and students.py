import math
sweets = float(input("Enter number of sweets:"))
students = float(input("Enter number of students:"))

def distribute(sweets, students):

    print ("Each student will have: ",math.floor(sweets / students))
    print ("Remaining sweets:",math.floor(sweets % students))

distribute(sweets,students)


