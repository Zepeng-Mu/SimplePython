rabbits = [0, 1, 1]
life = 16
month = 98
born = [0, 1, 0]
add = 0

for i in range(3,month + 1):
    if i <= life:
        m = 1
        while m <= (i - 2):
            add += born[m]
            m += 1
        born.append(add)
        add = 0
    else:
        for n in range(i - life, i - 1):
            add += born[n]
        born.append(add)
        add = 0

for j in range(3,month + 1):
    if j <= life:
        for p in range(1, life + 1):
            add += born[p]
        rabbits.append(add)
        add = 0
    elif j > life:
        for q in range(j - life + 1, j + 1):
            add += born[q]
        rabbits.append(add)
        add = 0

print rabbits[-1]