
report = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
gamma = ""
epsilon = ""

for i in range(len(report[0])):
    zero = 0
    one = 0
    for output in report:
        if "0" == output[i]:
            zero = zero + 1
        elif "1" == output[i]:
            one = one + 1

    if zero > one:
        gamma = gamma + "0"
        epsilon += "1"
    else:
        gamma = gamma + "1"
        epsilon += "0"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

power_combustion = gamma * epsilon
print("Power combustion:", power_combustion)


