h_start, d_start = 0,0
commands_list = []
while True:
    command = input("Enter command:")
    commands_list.append(command)
    if command == "done":
        break

for com in commands_list:
    if "forward" in com:
        com = com.split()
        step = int(com[1])
        h_start = h_start + step
    elif "down" in com:
        com = com.split()
        step = int(com[1])
        d_start = d_start + step
    elif "up" in com:
        com = com.split()
        step = int(com[1])
        d_start = d_start - step

print("Horizontal:", h_start)
print("Depth:", d_start)
print(d_start * h_start)



