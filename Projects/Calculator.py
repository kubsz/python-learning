
eqn_list = list()
while True:
    eqn = input("Enter problem:")
    if eqn == "done":
        break
    eqn_list.append(eqn)

#split 1st no., operator and second number, add them to separate lists
def arithmetic_arranger(eqn_list,showtotal):

    if len(eqn_list) > 5:
        print("Error: Too many problems.")
        quit()
    line1_list = list()
    line2_list =list()
    for eqn in eqn_list:
        split_eqn = eqn.split()
        if len(split_eqn[0]) > 4 or len(split_eqn[2]) >4:
            print("Error: Numbers cannot be more than four digits.")
            quit()
        line1_list.append(split_eqn[0])
        line2_list.append(split_eqn[1] + " " + split_eqn[2])

    line1string = ""
    line2string = ""
    dashstring = ""
    totalsstring = ""
    for i in range(len(line1_list)):
        diff = len(line2_list[i]) - len(line1_list[i])
        line1string = line1string + (" "*diff) + line1_list[i] + ("    ")
        line2string = line2string + line2_list[i] + ("    ")
        dashstring = dashstring + ("-"*len(line2_list[i])) + "    "

        splitnum2 = line2_list[i].split()
        num2 = splitnum2[1]
        if "-" in line2_list[i]:
            try:
                total = int(line1_list[i]) - int(num2)
            except:
                print("Error: Numbers must only contain digits.")
                quit()
        elif "+" in line2_list[i]:
            try:
                total = int(line1_list[i]) + int(num2)
            except:
                print("Error: Equations must only contain digits.")
                quit()
        else:
            print("Error: Operator must be '+' or '-'.")
            quit()
        total = str(total)
        diff = len(line2_list[i]) - len(total)
        totalsstring = totalsstring + (" "*diff) + total + ("    ")

    print(line1string)
    print(line2string)
    print(dashstring)
    if showtotal == True:
        print(totalsstring)

arithmetic_arranger(eqn_list, False)
arithmetic_arranger(eqn_list, True)
