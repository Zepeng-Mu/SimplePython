rabbits = [0, 1, 1]
for month in range(3,29):
    print month
    rabbits.append(rabbits[month - 1] + 3 * rabbits[month - 2])
    month += 1
print rabbits