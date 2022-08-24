from itertools import count


depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
prev_depth = 0
count = 0
for depth in depths[1:]:
    if depth > prev_depth:
        count = count + 1
    prev_depth = depth
print(count)
